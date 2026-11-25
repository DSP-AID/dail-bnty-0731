#!/usr/bin/env python3
"""Per-team play-level metrics from ESPN season play-by-play (raw/espn/pb).

Computes success rate, explosiveness, EPA/play (EP grid fitted on this season's
own data — no free public EPA feed exists without an API key), field position,
turnovers and most-frequent ball handlers, plus opponent-adjusted versions.

Play start/end `yardLine` is absolute from the HOME team's goal line, so all
positions are converted to "yards from own goal" for the possessing team before
binning. Only line-of-scrimmage plays (pass/rush/sack) count for per-play
metrics; kickoffs, punts and field goals are excluded.

Usage: python3 pbmetrics.py [--raw ../raw/espn/pb] [--out data/team_play_metrics.json]
"""
import argparse
import glob
import json
import os
from collections import defaultdict

METRICS = ("success_rate", "explosive_rate", "ypp", "epa_per_play")
LOS = {"Pass Reception", "Rush", "Sack", "Pass Incompletion",
       "Passing Touchdown", "Rushing Touchdown"}
TO_TYPES = {"Interception", "Pass Interception Return", "Fumble Recovery (Opponent)"}


def ybin(y):
    return min(19, (max(1, y) - 1) // 5)


def dbin(dist):
    return 0 if dist <= 3 else 1 if dist <= 7 else 2 if dist <= 12 else 3


def load_games(pb_dir):
    games = []
    for p in sorted(glob.glob(os.path.join(pb_dir, "pb_*.json"))):
        try:
            d = json.load(open(p))
        except Exception:
            continue
        drives = (d.get("drives") or {}).get("previous") or []
        tids = {str(((dr.get("team") or {}).get("id")) or "") for dr in drives} - {""}
        away = ""
        comps = ((d.get("header") or {}).get("competitions") or [{}])[0]
        home = ""
        for c in (comps.get("competitors") or []):
            if c.get("homeAway") == "home":
                home = str(c.get("id"))
        if len(tids) != 2 or not drives or home not in tids:
            continue
        games.append({"event": os.path.basename(p)[3:-5], "tids": sorted(tids),
                      "home": home, "drives": drives})
    return games


def prog(g, tid, y):
    """absolute ESPN yardLine (measured from the HOME goal line) -> yards from the
    possessing team's own goal."""
    return y if tid == g["home"] else 100 - y


def fit_ep(games):
    """EP(down, dist bucket, own-progress bin) = points the drive's team scores from
    (and including) this play onward. Plays carry cumulative away/home scores, so
    per-play deltas within a drive give labels (only the drive's team scores there)."""
    cells = defaultdict(lambda: [0.0, 0])
    for g in games:
        prev_after = (0, 0)
        for dr in g["drives"]:
            plays = dr.get("plays") or []
            dtid = str(((dr.get("team") or {}).get("id")) or "")
            deltas = []
            pa, ph = prev_after
            for p in plays:
                a, h = p.get("awayScore"), p.get("homeScore")
                if a is None or h is None:
                    a, h = pa, ph
                deltas.append(max(0, (a - pa) + (h - ph)))
                pa, ph = a, h
            prev_after = (pa, ph)
            for i, p in enumerate(plays):
                s = p.get("start") or {}
                if not s.get("down"):
                    continue
                y = prog(g, dtid, s.get("yardLine") or 50)
                label = sum(deltas[i:])
                for key in ((s["down"], dbin(s.get("distance") or 10), ybin(y)),
                            (s["down"], None, ybin(y)), (None, None, ybin(y))):
                    cells[key][0] += label
                    cells[key][1] += 1
    grid = {k: v[0] / v[1] for k, v in cells.items() if v[1] >= 8}
    fb = sum(v[0] for v in cells.values()) / max(1, sum(v[1] for v in cells.values()))

    def ep(down, dist, y):
        for key in ((down, dbin(dist or 10), ybin(y)), (down, None, ybin(y)), (None, None, ybin(y))):
            if key in grid:
                return grid[key]
        return fb
    return ep


def count_games(games):
    n = defaultdict(int)
    for g in games:
        for tid in g["tids"]:
            n[tid] += 1
    return n


def season_stats(games, ep):
    ngames = count_games(games)
    acc = defaultdict(lambda: defaultdict(list))
    for g in games:
        for dr in g["drives"]:
            dtid = str(((dr.get("team") or {}).get("id")) or "")
            st = (dr.get("start") or {}).get("yardLine")
            if st and dtid:
                own = prog(g, dtid, st)
                acc[dtid]["starts"].append(own)
                for t2 in g["tids"]:
                    if t2 != dtid:
                        acc[t2]["forced"].append(100 - own)
            for p in dr.get("plays") or []:
                s, e = p.get("start") or {}, p.get("end") or {}
                if not s.get("down") or p.get("isPenalty"):
                    continue
                tp = str(((p.get("type") or {}).get("text")) or "")
                team = str(((s.get("team") or {}).get("id")) or "")
                a = acc[team]
                dist = s.get("distance") or 10
                e0 = ep(s["down"], dist, prog(g, team, s.get("yardLine") or 50))
                if tp in TO_TYPES:
                    a["to"].append(1)
                    a["epa"].append(-ep(1, 10, prog(g, team, e.get("yardLine") or 50)) - e0)
                    continue
                if tp not in LOS:
                    continue
                a["to"].append(0)
                d = 1 if team == g["home"] else -1
                gained = (e.get("yardLine") or s["yardLine"]) - s["yardLine"]
                gained *= d
                ed = ep(e.get("down") or 1, e.get("distance") or 10, prog(g, team, min(99, e.get("yardLine") or 50)))
                a["epa"].append(ed - e0)
                td = tp in ("Passing Touchdown", "Rushing Touchdown")
                fd = td or "1ST DOWN" in (p.get("text") or "").upper() or (e.get("down") == 1 and gained > 0)
                ok = fd or (s["down"] in (3, 4) and dist <= 2 and gained >= max(1, dist / 2))
                a["sr"].append(1 if ok else 0)
                a["ex"].append(1 if gained >= 15 else 0)
                a["yds"].append(gained)
    out = {}
    for tid, a in acc.items():
        n = max(1, len(a["sr"]))
        out[tid] = {"plays": n,
                    "success_rate": sum(a["sr"]) / n,
                    "explosive_rate": sum(a["ex"]) / n,
                    "ypp": sum(a["yds"]) / n,
                    "epa_per_play": sum(a["epa"]) / max(1, len(a["epa"])),
                    "turnovers_lost_per_game": sum(a["to"]) / max(1, ngames[tid]),
                    "field_pos_avg_start": sum(a["starts"]) / max(1, len(a["starts"])),
                    "forced_field_pos": sum(a["forced"]) / max(1, len(a["forced"]))}
    return out


def opponent_adjust(stats, games):
    oppv = defaultdict(lambda: defaultdict(list))
    for g in games:
        for tid in g["tids"]:
            opp = next(t for t in g["tids"] if t != tid)
            for m in METRICS:
                if opp in stats:
                    oppv[tid][m].append(stats[opp][m])
    out = {}
    for tid, s in stats.items():
        o = dict(s)
        for m, vs in oppv[tid].items():
            if vs:
                o["adj_" + m] = s[m] - sum(vs) / len(vs)
        out[tid] = o
    return out


def key_players(games):
    """ball handlers named in play text, most frequent first."""
    cnt = defaultdict(lambda: defaultdict(int))
    for g in sorted(games, key=lambda x: x["event"]):
        for dr in g["drives"]:
            tid = str(((dr.get("team") or {}).get("id")) or "")
            for p in dr.get("plays") or []:
                if p.get("isPenalty"):
                    continue
                tp = ((p.get("type") or {}).get("text") or "").lower()
                if "pass" not in tp and "rush" not in tp:
                    continue
                t = p.get("text") or ""
                seg = t.split(") ")[-1] if ") " in t else t
                for cut in (" pass", " rush"):
                    if cut in seg.lower():
                        seg = seg[:seg.lower().index(cut)]
                        break
                seg = seg.replace("No Huddle-Shotgun", "").replace("Shotgun", "").replace("No Huddle", "").strip()
                parts = seg.split(" ")
                if len(parts) >= 2 and parts[0].startswith("#"):
                    name = " ".join(parts[1:]).strip()
                    if 3 <= len(name) <= 30:
                        cnt[tid][name] += 1
    return {t: sorted(v.items(), key=lambda x: -x[1])[:5] for t, v in cnt.items()}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(here, "..", "raw", "espn", "pb"))
    ap.add_argument("--out", default=os.path.join(here, "data", "team_play_metrics.json"))
    args = ap.parse_args()

    games = load_games(args.raw)
    ep = fit_ep(games)
    stats = season_stats(games, ep)
    adj = opponent_adjust(stats, games)
    players = key_players(games)

    out = {"method": ("%d completed games of ESPN play-by-play. All positions converted from "
                      "absolute yardlines to yards-from-own-goal for the possessing team. EP grid "
                      "fitted on the same data (down x distance-bucket x 5-yard bin, >=8 samples, "
                      "hierarchical fallback); EPA/play uses line-of-scrimmage plays only, excludes "
                      "penalised plays, and scores turnovers as -EP(opponent at new position). "
                      "Success rate = first-down/TD conversion (3rd/4th &<=2 counts with >=half "
                      "distance). Explosive play = >=15 net yards. Field position = mean drive start "
                      "(yards from own goal) and forced_field_pos = mean opponent drive start measured "
                      "from our goal (higher = better defense). Opponent-adjusted metric = team value "
                      "minus the mean of its opponents' season values." % len(games)),
           "games_used": len(games), "teams": {}}
    for tid, s in adj.items():
        row = {"plays": s["plays"]}
        for m in METRICS + tuple("adj_" + m for m in METRICS):
            if m in s:
                row[m] = round(s[m], 4)
        row["turnovers_lost_per_game"] = round(s["turnovers_lost_per_game"], 2)
        row["field_pos_avg_start"] = round(s["field_pos_avg_start"], 1)
        row["forced_field_pos"] = round(s["forced_field_pos"], 1)
        row["key_players"] = [n for n, _ in players.get(tid, [])[:3]]
        out["teams"][tid] = row
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(out, open(args.out, "w"), indent=1)
    print("wrote", args.out, "teams:", len(out["teams"]), "games:", out["games_used"])


if __name__ == "__main__":
    main()
