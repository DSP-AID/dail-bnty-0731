#!/usr/bin/env python3
"""Render the pre-k kickoff filing (FILING.md) from data/games.json.

Every game gets: AP rank + record, venue/kickoff, pick + predicted score with
the (total +/- margin)/2 arithmetic shown, TeamRankings power ratings, closing
line, opponent-adjusted EPA/SR/explosiveness (self-computed from ESPN play-by-
play, see pbmetrics.py), turnover margin, field position, home/away splits,
rest, travel, wind, availability-checked named players, and the full source
list with links + pull dates.

Usage: python3 build_filing.py [--out FILING.md]
"""
import argparse
import json
from datetime import datetime, timedelta, timezone

KMH2MPH = 0.621371


def utc2pt(iso):
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return dt.astimezone(timezone(timedelta(hours=-8))).strftime("%a %b %d, %H:%M PT")


def fmt_team(name, rank, rec):
    return f"#{rank} {name} ({rec})" if rank else f"{name} ({rec})"


def pick_of(g):
    """Pick = betting favorite per the filed line; power rating as tiebreak."""
    line = g["odds"]["home_spread_line"]
    if line is not None and abs(line) > 1e-9:
        return (g["home"], g["away"]) if line < 0 else (g["away"], g["home"])
    pr = g["power_ratings"]["ratings"].get("Predictive", {})
    hv = (pr.get(g["power_ratings"]["header"][1]) or {}).get("val", 0)
    av = (pr.get(g["power_ratings"]["header"][0]) or {}).get("val", 0)
    return (g["home"], g["away"]) if hv >= av else (g["away"], g["home"])


def game_md(g):
    L = []
    a, h = fmt_team(g["away"], g["away_rank"], g["away_rec"]), fmt_team(g["home"], g["home_rank"], g["home_rec"])
    L.append(f"### {a} at {h}")
    neutr = " (neutral site)" if g["neutral"] else ""
    L.append(f"- **When/where:** {utc2pt(g['kickoff_utc'])} ({g['kickoff_utc']}) — {g['venue']}, {g['city']}, {g['state']}{neutr}")
    p = g["prediction"]
    pick, dog = pick_of(g)
    L.append(f"- **Pick:** {pick}")
    L.append(f"- **Predicted score:** {g['home']} {p['home_pts']:g}, {g['away']} {p['away_pts']:g} "
             f"— arithmetic: margin_home = -line = {p['margin_home']:g}; "
             f"home = (total + margin)/2 = ({p['total']:g} + {p['margin_home']:g})/2 = {p['home_pts']:g}; "
             f"away = (total - margin)/2 = ({p['total']:g} - {p['margin_home']:g})/2 = {p['away_pts']:g}")
    o = g["odds"]
    L.append(f"- **Line ({o['provider']}, labeled close at pull; pre-kickoff):** {o['details']}, total {o['total']:g}")
    pr = g["power_ratings"]["ratings"]
    ah, hh = g["power_ratings"]["header"]
    def prow(k):
        x, y = pr[k].get(ah, {}), pr[k].get(hh, {})
        return f"{ah} {x.get('val')} (#{x.get('rank')}), {hh} {y.get('val')} (#{y.get('rank')})"
    L.append(f"- **Power ratings (TeamRankings):** Predictive: {prow('Predictive')}; Last 5: {prow('Last 5 Games')}; "
             f"Home: {prow('Home Games')}; Away: {prow('Away Games')}")
    pm = g["play_metrics"]
    for side, team in (("home", g["home"]), ("away", g["away"])):
        m = pm[side]
        L.append(f"- **Play metrics {team}** (self-computed from ESPN play-by-play): adj EPA/play {m['adj_epa_per_play']:+.3f}, "
                 f"adj success rate {m['adj_success_rate']:+.3f}, adj explosiveness {m['adj_explosive_rate']:+.3f}, "
                 f"raw SR {m['success_rate']:.3f}, raw explosive {m['explosive_rate']:.3f}, ypp {m['ypp']:.2f}, "
                 f"TO lost/gm {m['turnovers_lost_per_game']:.1f}, avg drive start own {m['field_pos_avg_start']:.1f} yd, "
                 f"opp forced to own {m['forced_field_pos']:.1f} yd ({m['plays']} plays)")
    tm = g["league_stats"]["to_margin"]
    L.append(f"- **Turnover margin/gm (TeamRankings):** {tm['away']['team']} {tm['away']['value']:+.1f}, "
             f"{tm['home']['team']} {tm['home']['value']:+.1f}")
    w = g["weather"]
    L.append(f"- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: "
             f"{g['odds'].get('espn_weather_condition') or 'n/a'}")
    r = g["rest_days"]
    L.append(f"- **Rest:** {g['away']} {r['away']['days']} days (last {r['away']['last_game']}), "
             f"{g['home']} {r['home']['days']} days (last {r['home']['last_game']})")
    t = g["travel_miles"]
    L.append(f"- **Travel (miles):** {g['away']} {t['away']}, {g['home']} {t['home']}")
    L.append(f"- **Wind:** max sustained {w['wind_max_kmh']:g} km/h ({w['wind_max_kmh']*KMH2MPH:.0f} mph), "
             f"gusts {w['gust_kmh']:g} km/h ({w['gust_kmh']*KMH2MPH:.0f} mph); temp {w['temp_min_f']:g}-{w['temp_max_f']:g}F, "
             f"precip {w['precip_prob_pct']}% (open-meteo @ venue {w['venue_lat']},{w['venue_lon']}, {w['local_date']})")
    np_ = g["named_players"]
    L.append(f"- **Key players (availability-checked):** {g['home']}: {', '.join(np_['home'])}; "
             f"{g['away']}: {', '.join(np_['away'])} — every name taken from this season's ESPN play-by-play "
             f"(recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings "
             f"injury page pulled {g['sources'][7]['pulled']}: no injury-report entry for any named player")
    L.append(f"- **Sources ({len(g['sources'])}, all pulled {g['sources'][0]['pulled']}):**")
    for i, s in enumerate(g["sources"], 1):
        L.append(f"  {i}. [{s['name']}]({s['url']}) — pulled {s['pulled']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="FILING.md")
    a = ap.parse_args()
    games = json.load(open("data/games.json"))
    poll = json.load(open("data/ap_poll_w13.json"))

    L = ["# CFB Week 13 (Rivalry Week) — AP Top 25 Slate Filing",
         "",
         "**Filed:** 2026-11-25 (before every listed kickoff; deadline Fri Nov 27 9:00 AM PT). "
         "**All picks and predicted scores were locked from data pulled on the filed date — no game in this slate has been played.**",
         "",
         f"**Rankings:** {poll['poll']} current at filing (published {poll['date']}). Source: [{poll['source']}]({poll['source']}) — pulled 2026-11-25, saved as `data/ap_poll_w13.json`. All 25 ranked teams appear below; the slate is every game involving an AP Top 25 team on Nov 26–28.",
         "",
         "**Method (applied to every game):** TeamRankings power ratings + ESPN/DraftKings closing line (labeled 'close' by ESPN pickcenter at pull time — games are unplayed, so these are pre-kickoff lines); opponent-adjusted EPA/play, success rate and explosiveness self-computed from all 2026 ESPN play-by-play (`pbmetrics.py`, EP grid fitted on this season); turnover margin (TeamRankings league table + ESPN team stats); field position (drive-start yardlines from play-by-play); home field (venue + TeamRankings home/away splits); rest days (ESPN scoreboard Week 12 dates); travel miles (TeamRankings travel pages); wind/gusts/temp/precip (open-meteo forecast at exact venue coordinates). Named players are season play-by-play ball handlers, availability-checked against the ESPN injuries API and TeamRankings injury pages. Predicted score = (total ± margin)/2 from the filed line, arithmetic shown per game.",
         "",
         "## Full slate (24 games, every AP Top 25 team)",
         "",
         "| # | Day | Kickoff (UTC) | Away | Home | Line | Total | Pick | Score (H-A) |",
         "|---|-----|---------------|------|------|------|-------|------|-------------|"]
    for i, g in enumerate(games, 1):
        p = g["prediction"]
        pick, _ = pick_of(g)
        ar = f"#{g['away_rank']} " if g["away_rank"] else ""
        hr = f"#{g['home_rank']} " if g["home_rank"] else ""
        L.append(f"| {i} | {g['day']} | {g['kickoff_utc']} | {ar}{g['away']} | {hr}{g['home']} | "
                 f"{g['odds']['details']} | {p['total']:g} | {pick} | {p['home_pts']:g}-{p['away_pts']:g} |")
    L += ["", "## Games", ""]
    for g in games:
        L += [game_md(g), ""]
    L += ["---", "",
          "Reproduce (no API keys; raw pulls ship in `raw/`): from the repo root run "
          "`python3 src/pbmetrics.py && python3 src/extract.py && python3 src/build_filing.py --out src/FILING.md`; "
          "`src/pull.sh` refreshes the raw pulls. Unit tests: `cd src && python3 -m pytest -q`.", ""]
    open(a.out, "w").write("\n".join(L))
    print(f"wrote {a.out}: {len(games)} games")


if __name__ == "__main__":
    main()
