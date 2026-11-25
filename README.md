# DAiL bounty bnty_0731 — CFB Week 13 (Rivalry Week) AP Top 25 Slate Filing

Pre-kickoff filing of every college-football game involving an AP Top 25 team on
Thu Nov 26 – Sat Nov 28, 2026 (Week 13 rivalry week): 24 games covering all 25
ranked teams, with a pick and predicted score for each. Filed **2026-11-25**,
before every listed kickoff — no game in the slate has been played.

**The filing itself: [`src/FILING.md`](src/FILING.md)** (regenerable, see below).

## Layout

| Path | What it is |
|------|------------|
| `src/FILING.md` | The filed document: full slate table + per-game method numbers, pick, predicted score with (total ± margin)/2 arithmetic, named availability-checked players, 16 sources each with links + pull date. |
| `src/data/games.json` | The complete dataset behind the filing (24 games × all metrics). Real public data, pulled 2026-11-25. |
| `src/data/slate.json`, `src/data/ap_poll_w13.json`, `src/data/team_play_metrics.json` | Slate from ESPN scoreboard; AP Top 25 (published 2026-11-22, ESPN rankings API); self-computed per-team play metrics. |
| `raw/` | Every raw pull as fetched on 2026-11-25: ESPN scoreboard/summary/play-by-play/injuries JSON, TeamRankings matchup + stat pages, open-meteo geocoding + forecasts. No keys required by any endpoint. |
| `src/pull.sh` | Re-pulls everything from public endpoints (optional — the data is already shipped). |
| `src/pbmetrics.py` | Self-computes EPA/play, success rate, explosiveness (opponent-adjusted) and field position from all season ESPN play-by-play; EP grid fitted on this season. |
| `src/extract.py` | Builds `data/games.json` from `raw/` (parses TeamRankings HTML, ESPN JSON, weather; computes rest days, travel, predictions, named players + availability). |
| `src/build_filing.py` | Renders `FILING.md` from `data/games.json`. |
| `src/test_pipeline.py` | Unit tests (`python3 -m pytest -q src/…`, 8 tests): prediction arithmetic, EP/SR/explosive/field-position math on a synthetic game, season-record derivation, HTML helpers. |

## Method (applied to every game)

Power ratings (TeamRankings predictive/last-5/home/away) + the closing line
(ESPN pickcenter, provider-labeled, marked "close" at pull); opponent-adjusted
EPA/play, success rate and explosiveness self-computed from 386 completed
2026 ESPN play-by-play games; turnover margin and yards/play etc. (TeamRankings
league tables + ESPN stats); field position (drive-start yardlines from
play-by-play); home field (venue + TeamRankings home/away splits); rest days
(ESPN Week 12 dates); travel miles (TeamRankings travel pages); wind/gusts/
temp/precip (open-meteo forecast at exact venue coordinates). Named players are
this season's play-by-play ball handlers, cross-checked against the ESPN league
injuries API and TeamRankings injury pages — zero flagged. Predicted score =
(total ± margin)/2 from the filed line, arithmetic shown per game. Pick = the
filed favorite (power rating as tiebreak).

## Reproduce (no API keys)

```bash
python3 src/pbmetrics.py            # raw/espn/pb -> src/data/team_play_metrics.json
python3 src/extract.py              # raw/ + slate -> src/data/games.json
python3 src/build_filing.py --out src/FILING.md   # games.json -> the filing
cd src && python3 -m pytest -q      # unit tests
```

`src/pull.sh` (run from this directory) refreshes `raw/` from public endpoints.
