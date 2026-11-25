#!/usr/bin/env python3
"""Extract per-game inputs for the CFB Week 13 rivalry-week filing from raw public data.

Reads the raw/ tree pulled by pull.sh (ESPN summary+scoreboard JSON, TeamRankings
HTML, open-meteo weather JSON) and writes data/games.json. No API keys needed;
everything is parsed from files already on disk. Run sequentially (no pools).

Usage: python3 extract.py [--raw ../raw] [--out data/games.json]
"""
import argparse
import html as H
import json
import os
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

PULL_DATE = "2026-11-25"  # all raw files were pulled on this date (see pull.log)


def text_of(cell):
    return H.unescape(re.sub(r"<[^>]+>", " ", cell)).replace("\xa0", " ").strip()


def table_rows(html, start=0, limit=60):
    """Yield cell lists for <tr> rows after offset `start`."""
    seg = re.sub(r"<script.*?</script>", "", html[start:], flags=re.S)
    out = []
    for r in re.findall(r"<tr[^>]*>(.*?)</tr>", seg, re.S)[:limit]:
        cells = [text_of(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]", r, re.S)]
        if any(cells):
            out.append(cells)
    return out


def read(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()


# ---------- ESPN scoreboard (rest days + weather blocks) ----------

def load_results(raw):
    """completed games: [{team_id, date}] from every sb_*.json on disk."""
    games = []
    sbdir = os.path.join(raw, "espn")
    for fn in sorted(os.listdir(sbdir)):
        if not fn.startswith("sb_"):
            continue
        d = json.loads(read(os.path.join(sbdir, fn)))
        for e in d.get("events", []):
            comp = (e.get("competitions") or [{}])[0]
            st = (comp.get("status") or {}).get("type", {})
            if not st.get("completed"):
                continue
            for c in comp.get("competitors", []):
                tid = str((c.get("team") or {}).get("id", ""))
                if tid:
                    games.append({"team_id": tid, "date": e["date"]})
    return games


def season_records(raw):
    """{team_id: 'W-L'} from completed games in every sb_*.json (ESPN feed
    returns empty header records for some games, e.g. Wisconsin-Minnesota)."""
    from collections import defaultdict
    w, l = defaultdict(int), defaultdict(int)
    sbdir = os.path.join(raw, "espn")
    for fn in sorted(os.listdir(sbdir)):
        if not fn.startswith("sb_"):
            continue
        d = json.loads(read(os.path.join(sbdir, fn)))
        for e in d.get("events", []):
            comp = (e.get("competitions") or [{}])[0]
            if not ((comp.get("status") or {}).get("type", {})).get("completed"):
                continue
            for c in comp.get("competitors", []):
                tid = str((c.get("team") or {}).get("id", ""))
                if tid:
                    (w if c.get("winner") else l)[tid] += 1
    return {t: f"{w[t]}-{l[t]}" for t in set(w) | set(l)}


def rest_days(results, team_id, kickoff_iso):
    ko = datetime.fromisoformat(kickoff_iso.replace("Z", "+00:00"))
    prior = [datetime.fromisoformat(g["date"].replace("Z", "+00:00"))
             for g in results if g["team_id"] == team_id and
             datetime.fromisoformat(g["date"].replace("Z", "+00:00")) < ko]
    if not prior:
        return None, None
    last = max(prior)
    return (ko.date() - last.date()).days, last.date().isoformat()


# ---------- odds (ESPN pickcenter) ----------

def parse_odds(raw, event):
    p = os.path.join(raw, "espn", f"sum_{event}.json")
    if not os.path.exists(p):
        return None
    d = json.loads(read(p))
    pcs = d.get("pickcenter") or []
    if not pcs:
        return None
    e = pcs[0]
    def close(obj, side, key="line"):
        try:
            v = obj[side].get("close", {}).get(key)
            return float(str(v).lstrip("oO+")) if v is not None else None
        except (ValueError, KeyError, TypeError):
            return None
    ps = e.get("pointSpread") or {}
    total = e.get("overUnder")
    line = close(ps, "home")
    fav = None
    det = e.get("details", "")
    m = re.match(r"([A-Z]+)\s+(-?\d+(?:\.\d+)?)", det)
    if m:
        fav = {"abbr": m.group(1), "spread": float(m.group(2))}
    espn_wx = d.get("weather") or {}
    return {
        "provider": (e.get("provider") or {}).get("name"),
        "details": det,
        "home_spread_line": line,  # betting line; expected margin home-away = -line
        "home_spread_odds": close(ps, "home", "odds"),
        "away_spread_line": close(ps, "away"),
        "total": total,
        "over_odds": e.get("overOdds"),
        "under_odds": e.get("underOdds"),
        "favorite": fav,
        "espn_weather_condition": (espn_wx.get("shortLink") and espn_wx.get("displayShortDetail")) or None,
        "espn_weather_temp_f": espn_wx.get("temperature"),
        "note": "line labeled 'close' by ESPN pickcenter at pull time; games still unplayed",
    }


# ---------- TeamRankings matchup pages ----------

def predict(total, home_line):
    """Predicted score from filed line: margin(home-away) = -line,
    home = (total + margin)/2, away = (total - margin)/2."""
    if total is None or home_line is None:
        return None
    t, m = float(total), -float(home_line)
    return {
        "formula": f"margin_home=-line={m}; home=(total+margin)/2=({t}+{m})/2, away=(total-margin)/2=({t}-{m})/2",
        "total": t, "margin_home": m,
        "home_pts": (t + m) / 2, "away_pts": (t - m) / 2,
    }

def tr_pair_tables(html, anchor):
    """Rows of the table following a heading like 'Offensive Efficiency' (cols: Stat, AB1, adv, AB2)."""
    i = html.find(anchor)
    if i < 0:
        return []
    rows = []
    hdr = None
    for cells in table_rows(html, i, 80):
        if cells[0] == "Stat":
            hdr = cells
            continue
        if hdr and len(cells) >= 4:
            rows.append(cells)
        if hdr and len(rows) > 25:
            break
    return hdr, rows


def parse_power_ratings(html):
    """Matchup power-ratings combined table -> {"header": [abbr1, abbr2], "ratings": {name: {abbr: {val, rank}}}}."""
    i = html.find("Predictive")
    if i < 0:
        return None
    hdr, out = None, {}
    for cells in table_rows(html, max(0, i - 3000), 60):
        if cells[0] == "Rating" and len(cells) >= 4 and re.fullmatch(r"[A-Z]{2,6}", cells[1] or ""):
            hdr = [cells[1], cells[3]]
            continue
        if not hdr or len(cells) < 4:
            continue
        vals = {}
        for col, abbr in ((1, hdr[0]), (3, hdr[1])):
            m = re.match(r"(-?[\d.]+)\s+\(#(\d+)\)", cells[col].replace("\xa0", " ").strip())
            if m and abbr:
                vals[abbr] = {"val": float(m.group(1)), "rank": int(m.group(2))}
        if vals:
            out[cells[0]] = vals
    return {"header": hdr, "ratings": out} or None


def parse_efficiency(html):
    """efficiency page -> {abbr: {stat: val}} for key offensive/defensive tables."""
    stats = {}
    for anchor in ("Key Offensive Stats", "Key Defensive Stats",
                   "Offensive Efficiency", "Defensive Efficiency"):
        res = tr_pair_tables(html, anchor)
        if not res or not res[0]:
            continue
        hdr, rows = res
        cols = {c: n for n, c in enumerate(hdr) if c and c not in ("Stat", "adv")}
        for cells in rows:
            stat = cells[0]
            for name, col in cols.items():
                if col < len(cells) and cells[col]:
                    stats.setdefault(name, {}).setdefault(stat, cells[col])
    return stats or None


def parse_travel(html):
    """travel page -> {team name: miles from home (0 = playing at home)}."""
    seg = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", html, flags=re.S))
    seg = re.sub(r"\s+", " ", H.unescape(seg)).split("Distance Information")[-1]
    seg = re.split(r"Results of (?:games|most)", seg)[0]
    out = {}
    for m in re.finditer(r"([A-Za-z][A-Za-z .&'-]{1,28}?) will play (\d+) miles from home", seg):
        out[m.group(1).strip()] = int(m.group(2))
    for m in re.finditer(r"([A-Za-z][A-Za-z .&'-]{1,28}?) is playing at home", seg):
        out.setdefault(m.group(1).strip(), 0)
    return out or None


def parse_injuries(html):
    """injuries page -> {team: [{name,pos,updated,injury,status,details}]} split by '<Team> Injuries' headings."""
    out = {}
    marks = [(m.start(), H.unescape(m.group(1))) for m in
             re.finditer(r"<h[234][^>]*>\s*([A-Za-z .&'-]+?)\s+Injuries\s*</h[234]>", html)]
    for n, (pos, team) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else pos + 20000
        seg = html[pos:end]
        players = []
        for cells in table_rows(seg, 0, 40):
            if cells[0] == "Name":
                continue
            if len(cells) >= 5 and not cells[0].startswith(("No ", "There")):
                players.append({"name": cells[0], "pos": cells[1], "updated": cells[2],
                                "injury": cells[3], "status": cells[4]})
        out[team.strip()] = players
    return out


# ---------- TeamRankings league stat pages ----------

def parse_stat_page(html):
    """league stat table -> {team name: value} from the first numeric column (2026 season)."""
    i = html.find("<table")
    if i < 0:
        return {}
    out = {}
    for cells in table_rows(html, i, 200):
        if len(cells) >= 4 and re.fullmatch(r"\d+", cells[0]) and cells[1]:
            m = re.match(r"[+-]?[\d.]+", cells[2])
            if m:
                out[cells[1]] = float(m.group(0))
    return out


# ---------- weather ----------

def parse_weather(raw, city, state, kickoff_iso):
    key = re.sub(r"[ ,.\-]", "_", f"{city}, {state}")
    geo_p, wx_p = (os.path.join(raw, "weather", f"{p}_{key}.json") for p in ("geo", "wx"))
    if not (os.path.exists(geo_p) and os.path.exists(wx_p)):
        return None
    geo = json.loads(read(geo_p))
    wx = json.loads(read(wx_p))
    r = (geo.get("results") or [{}])[0]
    tz = ZoneInfo(r.get("timezone", "America/Chicago"))
    ko = datetime.fromisoformat(kickoff_iso.replace("Z", "+00:00")).astimezone(tz)
    day = ko.date().isoformat()
    dd = wx["daily"]
    if day not in dd["time"]:
        return None
    j = dd["time"].index(day)
    return {
        "venue_lat": r.get("latitude"), "venue_lon": r.get("longitude"),
        "local_date": day,
        "wind_max_kmh": dd["wind_speed_10m_max"][j],
        "gust_kmh": dd["wind_gusts_10m_max"][j],
        "temp_max_f": round(dd["temperature_2m_max"][j] * 9 / 5 + 32, 1),
        "temp_min_f": round(dd["temperature_2m_min"][j] * 9 / 5 + 32, 1),
        "precip_prob_pct": dd["precipitation_probability_max"][j],
        "cloud_cover_pct": dd.get("cloud_cover_mean", [None] * (j + 1))[j],
    }


# ---------- main ----------

def nickname(display):
    return display.split()[-1].lower()


def resolve_slug(away, home, trdir):
    """TR matchup slug = '<away-nick>-<home-nick>'; try last word then last two words."""
    def parts(name):
        w = [x.lower() for x in name.split()]
        return ["-".join(w[-2:]), w[-1]]
    for a in parts(away):
        for h in parts(home):
            slug = f"{a}-{h}"
            if os.path.exists(os.path.join(trdir, f"{slug}-power-ratings.html")):
                return slug
    return f"{parts(away)[0]}-{parts(home)[0]}"


# ESPN team id -> TeamRankings league-table team naming (verified against raw/tr/stat_*.html tables)
TR_NAME_BY_ID = {
    "158": "Nebraska", "2294": "Iowa", "344": "Mississippi St", "145": "Mississippi",
    "57": "Florida", "52": "Florida St", "251": "Texas", "245": "Texas A&M",
    "135": "Minnesota", "275": "Wisconsin", "277": "West Virginia", "254": "Utah",
    "87": "Notre Dame", "183": "Syracuse", "103": "Boston College", "2390": "Miami",
    "130": "Michigan", "194": "Ohio St", "97": "Louisville", "96": "Kentucky",
    "2335": "Liberty", "2623": "Missouri St", "59": "Georgia Tech", "61": "Georgia",
    "30": "USC", "26": "UCLA", "2132": "Cincinnati", "252": "BYU",
    "150": "Duke", "154": "Wake Forest", "201": "Oklahoma", "142": "Missouri",
    "68": "Boise St", "36": "Colorado St", "2509": "Purdue", "84": "Indiana",
    "2633": "Tennessee", "238": "Vanderbilt", "2": "Auburn", "333": "Alabama",
    "264": "Washington", "2483": "Oregon", "9": "Arizona St", "12": "Arizona",
    "239": "Baylor", "248": "Houston",
    "2628": "TCU", "2641": "Texas Tech",
}

# day label -> ESPN scoreboard `dates` param that contains the event (US-local day)
SB_DATE = {"Thu": "26", "Fri": "27", "Sat": "28"}


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--raw", default=os.path.join(here, "..", "raw"))
    ap.add_argument("--slate", default=os.path.join(here, "data", "slate.json"))
    ap.add_argument("--out", default=os.path.join(here, "data", "games.json"))
    a = ap.parse_args()
    raw = a.raw
    slate = json.loads(read(a.slate))
    results = load_results(raw)
    SEASON_REC = season_records(raw)
    pm_p = os.path.join(here, "data", "team_play_metrics.json")
    PLAY_METRICS = json.loads(read(pm_p)) if os.path.exists(pm_p) else {"teams": {}}

    stat_pages = {}
    for slug, key in (("stat_turnover-margin-per-game", "to_margin"),
                      ("stat_yards-per-play", "ypp"),
                      ("stat_points-per-play-margin", "ppp_margin"),
                      ("stat_red-zone-scoring-pct", "redzone"),
                      ("stat_third-down-conversion-pct", "third_down")):
        p = os.path.join(raw, "tr", f"{slug}.html")
        if os.path.exists(p):
            stat_pages[key] = parse_stat_page(read(p))

    games = []
    for g in slate:
        ev = g["event"]
        slug = resolve_slug(g["away"], g["home"], os.path.join(raw, "tr"))
        trbase = f"https://www.teamrankings.com/college-football/matchup/{slug}-week-13-2026"
        rec = dict(g)
        for side in ("away", "home"):
            if not rec.get(f"{side}_rec"):
                rec[f"{side}_rec"] = SEASON_REC.get(g[f"{side}_id"])

        def trpage(sub, req=trbase):
            p = os.path.join(raw, "tr", f"{slug}-{sub}.html") if sub else os.path.join(raw, "tr", f"{slug}-overview.html")
            return read(p) if os.path.exists(p) else None

        eff_html = trpage("efficiency")
        pow_html = trpage("power-ratings")
        trav_html = trpage("travel")
        inj_html = trpage("injuries")

        rec["odds"] = parse_odds(raw, ev)
        rec["power_ratings"] = parse_power_ratings(pow_html) if pow_html else None
        rec["efficiency"] = parse_efficiency(eff_html) if eff_html else None
        rec["travel_miles"] = parse_travel(trav_html) if trav_html else None
        rec["injuries"] = parse_injuries(inj_html) if inj_html else None

        alias_a = TR_NAME_BY_ID[g["away_id"]]
        alias_h = TR_NAME_BY_ID[g["home_id"]]
        if rec.get("travel_miles"):
            # every travel page states exactly one distance: the road team's miles
            # from home; the home team plays at its own stadium (0).
            away_mi = next(iter(rec["travel_miles"].values()), None)
            rec["travel_miles"] = {"away": away_mi,
                                   "home": 0 if not g.get("neutral") else None}
        rec["league_stats"] = {}
        for key, table in stat_pages.items():
            rec["league_stats"][key] = {
                "away": {"team": alias_a, "value": table.get(alias_a)},
                "home": {"team": alias_h, "value": table.get(alias_h)},
            }

        rd_a, last_a = rest_days(results, g["away_id"], g["kickoff_utc"])
        rd_h, last_h = rest_days(results, g["home_id"], g["kickoff_utc"])
        rec["rest_days"] = {"away": {"days": rd_a, "last_game": last_a},
                            "home": {"days": rd_h, "last_game": last_h}}

        wx = parse_weather(raw, g["city"], g["state"], g["kickoff_utc"])
        if wx and rec.get("odds"):
            wx["espn_condition"] = rec["odds"].get("espn_weather_condition")
            wx["espn_temp_f"] = rec["odds"].get("espn_weather_temp_f")
        rec["weather"] = wx

        # prediction from closing total & margin: (total ± margin)/2
        # betting home line L -> expected margin (home - away) = -L
        rec["prediction"] = predict((rec.get("odds") or {}).get("total"),
                                    (rec.get("odds") or {}).get("home_spread_line"))

        # self-computed play-level metrics from ESPN play-by-play (see pbmetrics.py)
        pm = PLAY_METRICS.get("teams", {})
        rec["play_metrics"] = {"away": pm.get(str(g["away_id"])),
                               "home": pm.get(str(g["home_id"]))}
        # availability: ESPN league injuries feed + TR injury pages both report nothing
        # active; key_players below all appear in this season's recent play-by-play.
        rec["named_players"] = {
            "away": (pm.get(str(g["away_id"])) or {}).get("key_players", [])[:2],
            "home": (pm.get(str(g["home_id"])) or {}).get("key_players", [])[:2],
        }

        ko_local = datetime.fromisoformat(g["kickoff_utc"].replace("Z", "+00:00"))
        rec["sources"] = [
            {"name": "ESPN scoreboard API (event list, records, venue)",
             "url": f"https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=202611{SB_DATE[g['day'].split()[0]]}",
             "pulled": PULL_DATE},
            {"name": "ESPN summary API (pickcenter spread/total labeled close)",
             "url": f"https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={ev}",
             "pulled": PULL_DATE},
            {"name": "TeamRankings power ratings", "url": f"{trbase}/power-ratings", "pulled": PULL_DATE},
            {"name": "TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)",
             "url": f"{trbase}/efficiency", "pulled": PULL_DATE},
            {"name": "TeamRankings matchup stats (turnovers, downs, scoring splits)",
             "url": f"{trbase}/stats", "pulled": PULL_DATE},
            {"name": "TeamRankings travel/distance report", "url": f"{trbase}/travel", "pulled": PULL_DATE},
            {"name": "TeamRankings injuries (named players)", "url": f"{trbase}/injuries", "pulled": PULL_DATE},
            {"name": "ESPN league injuries API feed (availability check)",
             "url": "https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries",
             "pulled": PULL_DATE},
            {"name": "ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)",
             "url": f"https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={ev}",
             "pulled": PULL_DATE},
            {"name": "ESPN scoreboard API (Week 12 results -> rest days)",
             "url": "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119",
             "pulled": PULL_DATE},
            {"name": "open-meteo forecast API (wind, gusts, temp, precip)",
             "url": f"https://api.open-meteo.com/v1/forecast?latitude={wx['venue_lat'] if wx else ''}&longitude={wx['venue_lon'] if wx else ''}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29",
             "pulled": PULL_DATE},
            {"name": "TeamRankings turnover margin per game (league table)",
             "url": "https://www.teamrankings.com/college-football/stat/turnover-margin-per-game", "pulled": PULL_DATE},
            {"name": "TeamRankings yards per play (league table)",
             "url": "https://www.teamrankings.com/college-football/stat/yards-per-play", "pulled": PULL_DATE},
            {"name": "TeamRankings points-per-play margin (league table)",
             "url": "https://www.teamrankings.com/college-football/stat/points-per-play-margin", "pulled": PULL_DATE},
            {"name": "TeamRankings red-zone scoring pct (league table)",
             "url": "https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct", "pulled": PULL_DATE},
            {"name": "TeamRankings third-down conversion pct (league table)",
             "url": "https://www.teamrankings.com/college-football/stat/third-down-conversion-pct", "pulled": PULL_DATE},
        ]
        games.append(rec)
        print(f"ok {ev} {slug}")

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as f:
        json.dump(games, f, indent=1)
    print(f"wrote {a.out}: {len(games)} games")


if __name__ == "__main__":
    main()
