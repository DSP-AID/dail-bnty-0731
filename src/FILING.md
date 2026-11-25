# CFB Week 13 (Rivalry Week) — AP Top 25 Slate Filing

**Filed:** 2026-11-25 (before every listed kickoff; deadline Fri Nov 27 9:00 AM PT). **All picks and predicted scores were locked from data pulled on the filed date — no game in this slate has been played.**

**Rankings:** AP Top 25 current at filing (published 2026-11-22T08:00Z). Source: [https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2026/types/2/weeks/13/rankings/1?lang=en&region=us](https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2026/types/2/weeks/13/rankings/1?lang=en&region=us) — pulled 2026-11-25, saved as `data/ap_poll_w13.json`. All 25 ranked teams appear below; the slate is every game involving an AP Top 25 team on Nov 26–28.

**Method (applied to every game):** TeamRankings power ratings + ESPN/DraftKings closing line (labeled 'close' by ESPN pickcenter at pull time — games are unplayed, so these are pre-kickoff lines); opponent-adjusted EPA/play, success rate and explosiveness self-computed from all 2026 ESPN play-by-play (`pbmetrics.py`, EP grid fitted on this season); turnover margin (TeamRankings league table + ESPN team stats); field position (drive-start yardlines from play-by-play); home field (venue + TeamRankings home/away splits); rest days (ESPN scoreboard Week 12 dates); travel miles (TeamRankings travel pages); wind/gusts/temp/precip (open-meteo forecast at exact venue coordinates). Named players are season play-by-play ball handlers, availability-checked against the ESPN injuries API and TeamRankings injury pages. Predicted score = (total ± margin)/2 from the filed line, arithmetic shown per game.

## Full slate (24 games, every AP Top 25 team)

| # | Day | Kickoff (UTC) | Away | Home | Line | Total | Pick | Score (H-A) |
|---|-----|---------------|------|------|------|-------|------|-------------|
| 1 | Thu Nov 26 | 2026-11-27T01:00Z | TCU Horned Frogs | #9 Texas Tech Red Raiders | TTU -14 | 47.5 | Texas Tech Red Raiders | 30.75-16.75 |
| 2 | Fri Nov 27 | 2026-11-27T17:00Z | Nebraska Cornhuskers | #13 Iowa Hawkeyes | IOWA -4.5 | 40.5 | Iowa Hawkeyes | 22.5-18 |
| 3 | Fri Nov 27 | 2026-11-27T17:00Z | Mississippi State Bulldogs | #23 Ole Miss Rebels | MISS -18.5 | 56.5 | Ole Miss Rebels | 37.5-19 |
| 4 | Fri Nov 27 | 2026-11-27T20:30Z | #20 Florida Gators | Florida State Seminoles | FLA -6 | 53.5 | Florida Gators | 23.75-29.75 |
| 5 | Fri Nov 27 | 2026-11-28T00:30Z | #5 Texas Longhorns | Texas A&M Aggies | TEX -10.5 | 40.5 | Texas Longhorns | 15-25.5 |
| 6 | Fri Nov 27 | 2026-11-28T00:30Z | Minnesota Golden Gophers | Wisconsin Badgers | WIS -7.5 | 37.5 | Wisconsin Badgers | 22.5-15 |
| 7 | Fri Nov 27 | 2026-11-28T02:00Z | West Virginia Mountaineers | #2 Utah Utes | UTAH -22.5 | 68.5 | Utah Utes | 45.5-23 |
| 8 | Sat Nov 28 | 2026-11-28T17:00Z | #3 Notre Dame Fighting Irish | Syracuse Orange | ND -24.5 | 52.5 | Notre Dame Fighting Irish | 14-38.5 |
| 9 | Sat Nov 28 | 2026-11-28T17:00Z | Boston College Eagles | #4 Miami Hurricanes | MIA -25.5 | 53.5 | Miami Hurricanes | 39.5-14 |
| 10 | Sat Nov 28 | 2026-11-28T17:00Z | Michigan Wolverines | #25 Ohio State Buckeyes | OSU -10.5 | 38.5 | Ohio State Buckeyes | 24.5-14 |
| 11 | Sat Nov 28 | 2026-11-28T17:00Z | #18 Louisville Cardinals | Kentucky Wildcats | LOU -3 | 54.5 | Louisville Cardinals | 25.75-28.75 |
| 12 | Sat Nov 28 | 2026-11-28T19:00Z | #21 Liberty Flames | Missouri State Bears | LIB -16.5 | 52.5 | Liberty Flames | 18-34.5 |
| 13 | Sat Nov 28 | 2026-11-28T20:30Z | Georgia Tech Yellow Jackets | #1 Georgia Bulldogs | UGA -35.5 | 55.5 | Georgia Bulldogs | 45.5-10 |
| 14 | Sat Nov 28 | 2026-11-28T20:30Z | #15 USC Trojans | #10 UCLA Bruins | USC -7 | 45.5 | USC Trojans | 19.25-26.25 |
| 15 | Sat Nov 28 | 2026-11-28T20:30Z | Cincinnati Bearcats | #11 BYU Cougars | BYU -15.5 | 56.5 | BYU Cougars | 36-20.5 |
| 16 | Sat Nov 28 | 2026-11-28T20:30Z | Duke Blue Devils | #8 Wake Forest Demon Deacons | WAKE -14.5 | 55.5 | Wake Forest Demon Deacons | 35-20.5 |
| 17 | Sat Nov 28 | 2026-11-28T21:15Z | #19 Oklahoma Sooners | #24 Missouri Tigers | MIZ -2.5 | 41.5 | Missouri Tigers | 22-19.5 |
| 18 | Sat Nov 28 | 2026-11-28T23:00Z | #22 Boise State Broncos | Colorado State Rams | BOIS -21 | 76.5 | Boise State Broncos | 27.75-48.75 |
| 19 | Sat Nov 28 | 2026-11-29T00:00Z | Purdue Boilermakers | #12 Indiana Hoosiers | IU -22.5 | 52.5 | Indiana Hoosiers | 37.5-15 |
| 20 | Sat Nov 28 | 2026-11-29T00:00Z | #7 Tennessee Volunteers | Vanderbilt Commodores | TENN -13.5 | 43.5 | Tennessee Volunteers | 15-28.5 |
| 21 | Sat Nov 28 | 2026-11-29T00:30Z | Auburn Tigers | #6 Alabama Crimson Tide | ALA -15.5 | 49.5 | Alabama Crimson Tide | 32.5-17 |
| 22 | Sat Nov 28 | 2026-11-29T00:30Z | Washington Huskies | #14 Oregon Ducks | ORE -14 | 50.5 | Oregon Ducks | 32.25-18.25 |
| 23 | Sat Nov 28 | 2026-11-29T02:00Z | Arizona State Sun Devils | #16 Arizona Wildcats | ARIZ -8.5 | 53.5 | Arizona Wildcats | 31-22.5 |
| 24 | Sat Nov 28 | 2026-11-29T02:30Z | Baylor Bears | #17 Houston Cougars | HOU -4.5 | 55.5 | Houston Cougars | 30-25.5 |

## Games

### TCU Horned Frogs (5-6) at #9 Texas Tech Red Raiders (10-1)
- **When/where:** Thu Nov 26, 17:00 PT (2026-11-27T01:00Z) — Galaxy Stadium, Lubbock, TX
- **Pick:** Texas Tech Red Raiders
- **Predicted score:** Texas Tech Red Raiders 30.75, TCU Horned Frogs 16.75 — arithmetic: margin_home = -line = 14; home = (total + margin)/2 = (47.5 + 14)/2 = 30.75; away = (total - margin)/2 = (47.5 - 14)/2 = 16.75
- **Line (DraftKings, labeled close at pull; pre-kickoff):** TTU -14, total 47.5
- **Power ratings (TeamRankings):** Predictive: TCU 9.7 (#40), TTU 18.4 (#16); Last 5: TCU 7.2 (#52), TTU 17.6 (#16); Home: TCU 8.4 (#52), TTU 13.9 (#34); Away: TCU 15.2 (#28), TTU 20.9 (#16)
- **Play metrics Texas Tech Red Raiders** (self-computed from ESPN play-by-play): adj EPA/play -0.064, adj success rate +0.006, adj explosiveness +0.024, raw SR 0.330, raw explosive 0.139, ypp 6.79, TO lost/gm 1.7, avg drive start own 32.0 yd, opp forced to own 73.6 yd (409 plays)
- **Play metrics TCU Horned Frogs** (self-computed from ESPN play-by-play): adj EPA/play -0.174, adj success rate -0.040, adj explosiveness -0.013, raw SR 0.284, raw explosive 0.105, ypp 4.96, TO lost/gm 1.2, avg drive start own 28.6 yd, opp forced to own 71.6 yd (313 plays)
- **Turnover margin/gm (TeamRankings):** TCU -0.4, Texas Tech -0.1
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** TCU Horned Frogs 5 days (last 2026-11-22), Texas Tech Red Raiders 6 days (last 2026-11-21)
- **Travel (miles):** TCU Horned Frogs 267, Texas Tech Red Raiders 0
- **Wind:** max sustained 13 km/h (8 mph), gusts 24.1 km/h (15 mph); temp 23.9-51.1F, precip 0% (open-meteo @ venue 33.57786,-101.85517, 2026-11-26)
- **Key players (availability-checked):** Texas Tech Red Raiders: T.Castellanos, W.Hammond; TCU Horned Frogs: J.Craig, A.Schobel — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261126) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856879) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/horned-frogs-red-raiders-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/horned-frogs-red-raiders-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/horned-frogs-red-raiders-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/horned-frogs-red-raiders-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/horned-frogs-red-raiders-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856879) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=33.57786&longitude=-101.85517&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Nebraska Cornhuskers (7-4) at #13 Iowa Hawkeyes (9-2)
- **When/where:** Fri Nov 27, 09:00 PT (2026-11-27T17:00Z) — Kinnick Stadium, Iowa City, IA
- **Pick:** Iowa Hawkeyes
- **Predicted score:** Iowa Hawkeyes 22.5, Nebraska Cornhuskers 18 — arithmetic: margin_home = -line = 4.5; home = (total + margin)/2 = (40.5 + 4.5)/2 = 22.5; away = (total - margin)/2 = (40.5 - 4.5)/2 = 18
- **Line (DraftKings, labeled close at pull; pre-kickoff):** IOWA -4.5, total 40.5
- **Power ratings (TeamRankings):** Predictive: NEB 15.8 (#23), IOWA 18.7 (#14); Last 5: NEB 16.9 (#20), IOWA 24.9 (#7); Home: NEB 16.2 (#25), IOWA 18.5 (#21); Away: NEB 20.1 (#17), IOWA 21.6 (#13)
- **Play metrics Iowa Hawkeyes** (self-computed from ESPN play-by-play): adj EPA/play +0.040, adj success rate +0.047, adj explosiveness -0.013, raw SR 0.326, raw explosive 0.095, ypp 5.78, TO lost/gm 0.9, avg drive start own 31.0 yd, opp forced to own 75.5 yd (688 plays)
- **Play metrics Nebraska Cornhuskers** (self-computed from ESPN play-by-play): adj EPA/play +0.178, adj success rate +0.058, adj explosiveness +0.004, raw SR 0.337, raw explosive 0.104, ypp 5.71, TO lost/gm 0.6, avg drive start own 28.8 yd, opp forced to own 72.2 yd (778 plays)
- **Turnover margin/gm (TeamRankings):** Nebraska +0.7, Iowa -0.1
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Nebraska Cornhuskers 6 days (last 2026-11-21), Iowa Hawkeyes 6 days (last 2026-11-21)
- **Travel (miles):** Nebraska Cornhuskers 274, Iowa Hawkeyes 0
- **Wind:** max sustained 18.7 km/h (12 mph), gusts 37.4 km/h (23 mph); temp 30.7-45.3F, precip 15% (open-meteo @ venue 41.66113,-91.53017, 2026-11-27)
- **Key players (availability-checked):** Iowa Hawkeyes: H.Brown, L.Phillips Jr.; Nebraska Cornhuskers: A.Colandrea, J.Rule — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261127) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858536) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/cornhuskers-hawkeyes-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/cornhuskers-hawkeyes-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/cornhuskers-hawkeyes-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/cornhuskers-hawkeyes-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/cornhuskers-hawkeyes-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858536) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=41.66113&longitude=-91.53017&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Mississippi State Bulldogs (5-6) at #23 Ole Miss Rebels (7-4)
- **When/where:** Fri Nov 27, 09:00 PT (2026-11-27T17:00Z) — Vaught-Hemingway Stadium, Oxford, MS
- **Pick:** Ole Miss Rebels
- **Predicted score:** Ole Miss Rebels 37.5, Mississippi State Bulldogs 19 — arithmetic: margin_home = -line = 18.5; home = (total + margin)/2 = (56.5 + 18.5)/2 = 37.5; away = (total - margin)/2 = (56.5 - 18.5)/2 = 19
- **Line (DraftKings, labeled close at pull; pre-kickoff):** MISS -18.5, total 56.5
- **Power ratings (TeamRankings):** Predictive: MSST 6.8 (#49), MISS 20.8 (#13); Last 5: MSST -3.3 (#87), MISS 17.5 (#17); Home: MSST 2.5 (#72), MISS 21.5 (#14); Away: MSST 14.3 (#31), MISS 18.9 (#19)
- **Play metrics Ole Miss Rebels** (self-computed from ESPN play-by-play): adj EPA/play +0.062, adj success rate +0.063, adj explosiveness +0.029, raw SR 0.363, raw explosive 0.138, ypp 6.37, TO lost/gm 1.6, avg drive start own 28.1 yd, opp forced to own 71.1 yd (703 plays)
- **Play metrics Mississippi State Bulldogs** (self-computed from ESPN play-by-play): adj EPA/play +0.027, adj success rate +0.012, adj explosiveness +0.004, raw SR 0.301, raw explosive 0.108, ypp 5.55, TO lost/gm 1.2, avg drive start own 29.7 yd, opp forced to own 70.0 yd (713 plays)
- **Turnover margin/gm (TeamRankings):** Mississippi St -0.7, Mississippi -0.2
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Mississippi State Bulldogs 6 days (last 2026-11-21), Ole Miss Rebels 6 days (last 2026-11-21)
- **Travel (miles):** Mississippi State Bulldogs 76, Ole Miss Rebels 0
- **Wind:** max sustained 14.8 km/h (9 mph), gusts 43.9 km/h (27 mph); temp 35.4-52.5F, precip 0% (open-meteo @ venue 34.3665,-89.51925, 2026-11-27)
- **Key players (availability-checked):** Ole Miss Rebels: T.Chambliss, K.Lacy; Mississippi State Bulldogs: K.Taylor, P.Puckett — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261127) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856762) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/bulldogs-rebels-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/bulldogs-rebels-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/bulldogs-rebels-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/bulldogs-rebels-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/bulldogs-rebels-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856762) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=34.3665&longitude=-89.51925&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #20 Florida Gators (7-4) at Florida State Seminoles (5-6)
- **When/where:** Fri Nov 27, 12:30 PT (2026-11-27T20:30Z) — Doak Campbell Stadium, Tallahassee, FL
- **Pick:** Florida Gators
- **Predicted score:** Florida State Seminoles 23.75, Florida Gators 29.75 — arithmetic: margin_home = -line = -6; home = (total + margin)/2 = (53.5 + -6)/2 = 23.75; away = (total - margin)/2 = (53.5 - -6)/2 = 29.75
- **Line (DraftKings, labeled close at pull; pre-kickoff):** FLA -6, total 53.5
- **Power ratings (TeamRankings):** Predictive: FLA 16.7 (#20), FSU 6.9 (#48); Last 5: FLA 15.8 (#25), FSU 4.7 (#58); Home: FLA 16.5 (#24), FSU 2.4 (#74); Away: FLA 17.4 (#22), FSU 12.2 (#36)
- **Play metrics Florida State Seminoles** (self-computed from ESPN play-by-play): adj EPA/play -0.034, adj success rate +0.012, adj explosiveness +0.009, raw SR 0.313, raw explosive 0.117, ypp 5.73, TO lost/gm 1.6, avg drive start own 29.0 yd, opp forced to own 70.7 yd (686 plays)
- **Play metrics Florida Gators** (self-computed from ESPN play-by-play): adj EPA/play +0.109, adj success rate +0.021, adj explosiveness +0.003, raw SR 0.328, raw explosive 0.109, ypp 5.69, TO lost/gm 1.1, avg drive start own 30.3 yd, opp forced to own 70.9 yd (734 plays)
- **Turnover margin/gm (TeamRankings):** Florida -0.2, Florida St -0.8
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Florida Gators 6 days (last 2026-11-21), Florida State Seminoles 6 days (last 2026-11-21)
- **Travel (miles):** Florida Gators 129, Florida State Seminoles 0
- **Wind:** max sustained 15.6 km/h (10 mph), gusts 36 km/h (22 mph); temp 39.6-58.3F, precip 0% (open-meteo @ venue 30.43826,-84.28073, 2026-11-27)
- **Key players (availability-checked):** Florida State Seminoles: A.Daniels, O.Kromah; Florida Gators: A.Philo, J.Baugh — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261127) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856759) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/gators-seminoles-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/gators-seminoles-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/gators-seminoles-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/gators-seminoles-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/gators-seminoles-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856759) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=30.43826&longitude=-84.28073&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #5 Texas Longhorns (9-2) at Texas A&M Aggies (4-7)
- **When/where:** Fri Nov 27, 16:30 PT (2026-11-28T00:30Z) — Kyle Field, College Station, TX
- **Pick:** Texas Longhorns
- **Predicted score:** Texas A&M Aggies 15, Texas Longhorns 25.5 — arithmetic: margin_home = -line = -10.5; home = (total + margin)/2 = (40.5 + -10.5)/2 = 15; away = (total - margin)/2 = (40.5 - -10.5)/2 = 25.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** TEX -10.5, total 40.5
- **Power ratings (TeamRankings):** Predictive: TEX 29.0 (#3), TXAM 14.4 (#26); Last 5: TEX 33.0 (#3), TXAM 9.7 (#44); Home: TEX 30.7 (#2), TXAM 18.9 (#19); Away: TEX 30.8 (#4), TXAM 5.0 (#54)
- **Play metrics Texas A&M Aggies** (self-computed from ESPN play-by-play): adj EPA/play -0.029, adj success rate -0.006, adj explosiveness -0.006, raw SR 0.291, raw explosive 0.093, ypp 5.01, TO lost/gm 1.4, avg drive start own 30.6 yd, opp forced to own 72.6 yd (707 plays)
- **Play metrics Texas Longhorns** (self-computed from ESPN play-by-play): adj EPA/play -0.021, adj success rate -0.007, adj explosiveness -0.003, raw SR 0.310, raw explosive 0.105, ypp 5.46, TO lost/gm 1.1, avg drive start own 29.4 yd, opp forced to own 70.6 yd (703 plays)
- **Turnover margin/gm (TeamRankings):** Texas -0.2, Texas A&M +0.0
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Texas Longhorns 7 days (last 2026-11-21), Texas A&M Aggies 7 days (last 2026-11-21)
- **Travel (miles):** Texas Longhorns 86, Texas A&M Aggies 0
- **Wind:** max sustained 13.8 km/h (9 mph), gusts 35.6 km/h (22 mph); temp 41.7-62.4F, precip 0% (open-meteo @ venue 30.62798,-96.33441, 2026-11-27)
- **Key players (availability-checked):** Texas A&M Aggies: M.Reed, R.Owens II; Texas Longhorns: A.Manning, R.Brown — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261127) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856756) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/longhorns-aggies-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/longhorns-aggies-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/longhorns-aggies-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/longhorns-aggies-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/longhorns-aggies-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856756) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=30.62798&longitude=-96.33441&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Minnesota Golden Gophers (6-5) at Wisconsin Badgers (7-4)
- **When/where:** Fri Nov 27, 16:30 PT (2026-11-28T00:30Z) — Camp Randall Stadium, Madison, WI
- **Pick:** Wisconsin Badgers
- **Predicted score:** Wisconsin Badgers 22.5, Minnesota Golden Gophers 15 — arithmetic: margin_home = -line = 7.5; home = (total + margin)/2 = (37.5 + 7.5)/2 = 22.5; away = (total - margin)/2 = (37.5 - 7.5)/2 = 15
- **Line (DraftKings, labeled close at pull; pre-kickoff):** WIS -7.5, total 37.5
- **Power ratings (TeamRankings):** Predictive: MINN 5.4 (#56), WIS 13.4 (#31); Last 5: MINN 7.8 (#49), WIS 15.1 (#28); Home: MINN 7.7 (#54), WIS 20.0 (#16); Away: MINN -0.2 (#74), WIS 12.0 (#37)
- **Play metrics Wisconsin Badgers** (self-computed from ESPN play-by-play): adj EPA/play +0.060, adj success rate +0.003, adj explosiveness +0.024, raw SR 0.296, raw explosive 0.115, ypp 5.53, TO lost/gm 0.8, avg drive start own 30.0 yd, opp forced to own 72.6 yd (619 plays)
- **Play metrics Minnesota Golden Gophers** (self-computed from ESPN play-by-play): adj EPA/play -0.026, adj success rate -0.016, adj explosiveness +0.007, raw SR 0.268, raw explosive 0.109, ypp 4.91, TO lost/gm 0.8, avg drive start own 32.9 yd, opp forced to own 71.7 yd (672 plays)
- **Turnover margin/gm (TeamRankings):** Minnesota +0.7, Wisconsin -0.3
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Minnesota Golden Gophers 7 days (last 2026-11-21), Wisconsin Badgers 7 days (last 2026-11-21)
- **Travel (miles):** Minnesota Golden Gophers 230, Wisconsin Badgers 0
- **Wind:** max sustained 20 km/h (12 mph), gusts 41.4 km/h (26 mph); temp 31.3-46.2F, precip 22% (open-meteo @ venue 43.07305,-89.40123, 2026-11-27)
- **Key players (availability-checked):** Wisconsin Badgers: C.Joseph, D.Dupree; Minnesota Golden Gophers: D.Lindsey, D.Taylor — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261127) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858544) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/golden-gophers-badgers-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/golden-gophers-badgers-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/golden-gophers-badgers-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/golden-gophers-badgers-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/golden-gophers-badgers-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858544) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=43.07305&longitude=-89.40123&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### West Virginia Mountaineers (5-6) at #2 Utah Utes (11-0)
- **When/where:** Fri Nov 27, 18:00 PT (2026-11-28T02:00Z) — Rice-Eccles Stadium, Salt Lake City, UT
- **Pick:** Utah Utes
- **Predicted score:** Utah Utes 45.5, West Virginia Mountaineers 23 — arithmetic: margin_home = -line = 22.5; home = (total + margin)/2 = (68.5 + 22.5)/2 = 45.5; away = (total - margin)/2 = (68.5 - 22.5)/2 = 23
- **Line (DraftKings, labeled close at pull; pre-kickoff):** UTAH -22.5, total 68.5
- **Power ratings (TeamRankings):** Predictive: WVU 4.3 (#60), UTAH 21.7 (#12); Last 5: WVU 5.8 (#56), UTAH 24.8 (#8); Home: WVU -1.2 (#82), UTAH 25.2 (#9); Away: WVU 12.4 (#35), UTAH 21.9 (#12)
- **Play metrics Utah Utes** (self-computed from ESPN play-by-play): adj EPA/play +0.057, adj success rate +0.061, adj explosiveness +0.014, raw SR 0.364, raw explosive 0.122, ypp 6.33, TO lost/gm 1.1, avg drive start own 30.8 yd, opp forced to own 72.4 yd (736 plays)
- **Play metrics West Virginia Mountaineers** (self-computed from ESPN play-by-play): adj EPA/play +0.078, adj success rate +0.002, adj explosiveness +0.014, raw SR 0.312, raw explosive 0.126, ypp 5.89, TO lost/gm 0.6, avg drive start own 26.6 yd, opp forced to own 70.9 yd (810 plays)
- **Turnover margin/gm (TeamRankings):** West Virginia +0.1, Utah +0.3
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** West Virginia Mountaineers 7 days (last 2026-11-21), Utah Utes 6 days (last 2026-11-22)
- **Travel (miles):** West Virginia Mountaineers 1682, Utah Utes 0
- **Wind:** max sustained 9.2 km/h (6 mph), gusts 11.9 km/h (7 mph); temp 43.5-54.3F, precip 14% (open-meteo @ venue 40.76078,-111.89105, 2026-11-27)
- **Key players (availability-checked):** Utah Utes: D.Dampier, W.Parker; West Virginia Mountaineers: M.Hawkins Jr., C.Cook — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261127) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856880) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/mountaineers-utes-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/mountaineers-utes-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/mountaineers-utes-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/mountaineers-utes-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/mountaineers-utes-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856880) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=40.76078&longitude=-111.89105&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #3 Notre Dame Fighting Irish (10-1) at Syracuse Orange (5-6)
- **When/where:** Sat Nov 28, 09:00 PT (2026-11-28T17:00Z) — JMA Wireless Dome, Syracuse, NY
- **Pick:** Notre Dame Fighting Irish
- **Predicted score:** Syracuse Orange 14, Notre Dame Fighting Irish 38.5 — arithmetic: margin_home = -line = -24.5; home = (total + margin)/2 = (52.5 + -24.5)/2 = 14; away = (total - margin)/2 = (52.5 - -24.5)/2 = 38.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** ND -24.5, total 52.5
- **Power ratings (TeamRankings):** Predictive: ND 29.8 (#2), SYR 3.5 (#64); Last 5: ND 25.0 (#6), SYR 4.2 (#59); Home: ND 31.1 (#1), SYR 6.3 (#57); Away: ND 27.5 (#6), SYR 2.9 (#63)
- **Play metrics Syracuse Orange** (self-computed from ESPN play-by-play): adj EPA/play +0.008, adj success rate +0.024, adj explosiveness -0.001, raw SR 0.317, raw explosive 0.108, ypp 5.23, TO lost/gm 1.0, avg drive start own 30.1 yd, opp forced to own 72.5 yd (851 plays)
- **Play metrics Notre Dame Fighting Irish** (self-computed from ESPN play-by-play): adj EPA/play +0.170, adj success rate +0.073, adj explosiveness +0.010, raw SR 0.365, raw explosive 0.107, ypp 6.32, TO lost/gm 0.6, avg drive start own 29.8 yd, opp forced to own 73.6 yd (737 plays)
- **Turnover margin/gm (TeamRankings):** Notre Dame +1.4, Syracuse -0.1
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Notre Dame Fighting Irish 6 days (last 2026-11-22), Syracuse Orange 7 days (last 2026-11-21)
- **Travel (miles):** Notre Dame Fighting Irish 523, Syracuse Orange 0
- **Wind:** max sustained 19 km/h (12 mph), gusts 38.9 km/h (24 mph); temp 38.5-46.9F, precip 55% (open-meteo @ venue 43.04812,-76.14742, 2026-11-28)
- **Key players (availability-checked):** Syracuse Orange: S.Angeli, A.Miller; Notre Dame Fighting Irish: C.Carr, N.James Jr. — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858314) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/fighting-irish-orange-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/fighting-irish-orange-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/fighting-irish-orange-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/fighting-irish-orange-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/fighting-irish-orange-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858314) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=43.04812&longitude=-76.14742&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Boston College Eagles (5-6) at #4 Miami Hurricanes (10-1)
- **When/where:** Sat Nov 28, 09:00 PT (2026-11-28T17:00Z) — Hard Rock Stadium, Miami Gardens, FL
- **Pick:** Miami Hurricanes
- **Predicted score:** Miami Hurricanes 39.5, Boston College Eagles 14 — arithmetic: margin_home = -line = 25.5; home = (total + margin)/2 = (53.5 + 25.5)/2 = 39.5; away = (total - margin)/2 = (53.5 - 25.5)/2 = 14
- **Line (DraftKings, labeled close at pull; pre-kickoff):** MIA -25.5, total 53.5
- **Power ratings (TeamRankings):** Predictive: BC -2.5 (#83), MIA 27.5 (#5); Last 5: BC 0.8 (#72), MIA 21.8 (#13); Home: BC -0.8 (#81), MIA 25.3 (#8); Away: BC -3.0 (#80), MIA 31.3 (#3)
- **Play metrics Miami Hurricanes** (self-computed from ESPN play-by-play): adj EPA/play +0.215, adj success rate +0.121, adj explosiveness +0.042, raw SR 0.399, raw explosive 0.138, ypp 6.98, TO lost/gm 0.6, avg drive start own 29.0 yd, opp forced to own 71.6 yd (762 plays)
- **Play metrics Boston College Eagles** (self-computed from ESPN play-by-play): adj EPA/play -0.038, adj success rate -0.018, adj explosiveness +0.019, raw SR 0.292, raw explosive 0.123, ypp 5.45, TO lost/gm 1.4, avg drive start own 28.9 yd, opp forced to own 68.6 yd (667 plays)
- **Turnover margin/gm (TeamRankings):** Boston College +0.0, Miami +0.4
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Boston College Eagles 7 days (last 2026-11-21), Miami Hurricanes 6 days (last 2026-11-22)
- **Travel (miles):** Boston College Eagles 1243, Miami Hurricanes 0
- **Wind:** max sustained 15.2 km/h (9 mph), gusts 20.2 km/h (13 mph); temp 64.9-73.9F, precip 8% (open-meteo @ venue 25.94204,-80.2456, 2026-11-28)
- **Key players (availability-checked):** Miami Hurricanes: D.Mensah, M.Fletcher Jr.; Boston College Eagles: M.McKenzie, B.MacCormack III — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858311) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/eagles-hurricanes-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/eagles-hurricanes-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/eagles-hurricanes-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/eagles-hurricanes-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/eagles-hurricanes-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858311) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=25.94204&longitude=-80.2456&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Michigan Wolverines (6-5) at #25 Ohio State Buckeyes (7-4)
- **When/where:** Sat Nov 28, 09:00 PT (2026-11-28T17:00Z) — Ohio Stadium, Columbus, OH
- **Pick:** Ohio State Buckeyes
- **Predicted score:** Ohio State Buckeyes 24.5, Michigan Wolverines 14 — arithmetic: margin_home = -line = 10.5; home = (total + margin)/2 = (38.5 + 10.5)/2 = 24.5; away = (total - margin)/2 = (38.5 - 10.5)/2 = 14
- **Line (DraftKings, labeled close at pull; pre-kickoff):** OSU -10.5, total 38.5
- **Power ratings (TeamRankings):** Predictive: MICH 10.2 (#37), OSU 25.7 (#6); Last 5: MICH 6.4 (#55), OSU 16.0 (#23); Home: MICH 9.1 (#49), OSU 24.1 (#10); Away: MICH 4.4 (#58), OSU 24.1 (#10)
- **Play metrics Ohio State Buckeyes** (self-computed from ESPN play-by-play): adj EPA/play +0.120, adj success rate +0.076, adj explosiveness +0.042, raw SR 0.368, raw explosive 0.138, ypp 6.58, TO lost/gm 1.1, avg drive start own 29.3 yd, opp forced to own 69.1 yd (730 plays)
- **Play metrics Michigan Wolverines** (self-computed from ESPN play-by-play): adj EPA/play -0.034, adj success rate -0.012, adj explosiveness +0.003, raw SR 0.265, raw explosive 0.093, ypp 4.83, TO lost/gm 1.6, avg drive start own 29.5 yd, opp forced to own 69.5 yd (648 plays)
- **Turnover margin/gm (TeamRankings):** Michigan -0.7, Ohio St -0.3
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Michigan Wolverines 7 days (last 2026-11-21), Ohio State Buckeyes 7 days (last 2026-11-21)
- **Travel (miles):** Michigan Wolverines 161, Ohio State Buckeyes 0
- **Wind:** max sustained 18.4 km/h (11 mph), gusts 47.9 km/h (30 mph); temp 36.5-48F, precip 31% (open-meteo @ venue 39.96118,-82.99879, 2026-11-28)
- **Key players (availability-checked):** Ohio State Buckeyes: J.Sayin, B.Jackson; Michigan Wolverines: B.Underwood, T.Carr — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858540) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/wolverines-buckeyes-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/wolverines-buckeyes-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/wolverines-buckeyes-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/wolverines-buckeyes-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/wolverines-buckeyes-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858540) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=39.96118&longitude=-82.99879&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #18 Louisville Cardinals (8-3) at Kentucky Wildcats (7-4)
- **When/where:** Sat Nov 28, 09:00 PT (2026-11-28T17:00Z) — Kroger Field, Lexington, KY
- **Pick:** Louisville Cardinals
- **Predicted score:** Kentucky Wildcats 25.75, Louisville Cardinals 28.75 — arithmetic: margin_home = -line = -3; home = (total + margin)/2 = (54.5 + -3)/2 = 25.75; away = (total - margin)/2 = (54.5 - -3)/2 = 28.75
- **Line (DraftKings, labeled close at pull; pre-kickoff):** LOU -3, total 54.5
- **Power ratings (TeamRankings):** Predictive: LOU 18.6 (#15), UK 12.0 (#35); Last 5: LOU 23.5 (#11), UK 11.6 (#40); Home: LOU 23.5 (#11), UK 10.7 (#43); Away: LOU 15.3 (#27), UK 15.4 (#26)
- **Play metrics Kentucky Wildcats** (self-computed from ESPN play-by-play): adj EPA/play +0.025, adj success rate +0.020, adj explosiveness +0.013, raw SR 0.327, raw explosive 0.117, ypp 5.91, TO lost/gm 1.0, avg drive start own 30.4 yd, opp forced to own 70.8 yd (700 plays)
- **Play metrics Louisville Cardinals** (self-computed from ESPN play-by-play): adj EPA/play +0.095, adj success rate +0.049, adj explosiveness +0.031, raw SR 0.358, raw explosive 0.141, ypp 6.68, TO lost/gm 0.6, avg drive start own 32.2 yd, opp forced to own 70.5 yd (695 plays)
- **Turnover margin/gm (TeamRankings):** Louisville +1.0, Kentucky +0.7
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Louisville Cardinals 6 days (last 2026-11-22), Kentucky Wildcats 6 days (last 2026-11-22)
- **Travel (miles):** Louisville Cardinals 69, Kentucky Wildcats 0
- **Wind:** max sustained 27.9 km/h (17 mph), gusts 58.7 km/h (36 mph); temp 31.6-49.8F, precip 4% (open-meteo @ venue 37.98869,-84.47772, 2026-11-28)
- **Key players (availability-checked):** Kentucky Wildcats: K.Minchey, C.Baxter; Louisville Cardinals: L.Kienholz, I.Brown — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856761) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/cardinals-wildcats-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/cardinals-wildcats-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/cardinals-wildcats-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/cardinals-wildcats-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/cardinals-wildcats-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856761) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=37.98869&longitude=-84.47772&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #21 Liberty Flames (10-1) at Missouri State Bears (4-7)
- **When/where:** Sat Nov 28, 11:00 PT (2026-11-28T19:00Z) — Robert W. Plaster Stadium, Springfield, MO
- **Pick:** Liberty Flames
- **Predicted score:** Missouri State Bears 18, Liberty Flames 34.5 — arithmetic: margin_home = -line = -16.5; home = (total + margin)/2 = (52.5 + -16.5)/2 = 18; away = (total - margin)/2 = (52.5 - -16.5)/2 = 34.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** LIB -16.5, total 52.5
- **Power ratings (TeamRankings):** Predictive: LIB 3.3 (#66), MOSU -16.1 (#124); Last 5: LIB 9.1 (#46), MOSU -13.8 (#116); Home: LIB 4.1 (#68), MOSU -10.5 (#109); Away: LIB 8.6 (#45), MOSU -19.2 (#128)
- **Play metrics Missouri State Bears** (self-computed from ESPN play-by-play): adj EPA/play +0.086, adj success rate +0.000, adj explosiveness +0.007, raw SR 0.281, raw explosive 0.106, ypp 5.45, TO lost/gm 0.9, avg drive start own 26.3 yd, opp forced to own 68.2 yd (688 plays)
- **Play metrics Liberty Flames** (self-computed from ESPN play-by-play): adj EPA/play +0.197, adj success rate +0.105, adj explosiveness +0.037, raw SR 0.378, raw explosive 0.137, ypp 6.70, TO lost/gm 0.7, avg drive start own 32.3 yd, opp forced to own 72.5 yd (629 plays)
- **Turnover margin/gm (TeamRankings):** Liberty +0.5, Missouri St +0.0
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Liberty Flames 7 days (last 2026-11-21), Missouri State Bears 7 days (last 2026-11-21)
- **Travel (miles):** Liberty Flames 774, Missouri State Bears 0
- **Wind:** max sustained 19.7 km/h (12 mph), gusts 63.7 km/h (40 mph); temp 43-57.2F, precip 8% (open-meteo @ venue 37.21533,-93.29824, 2026-11-28)
- **Key players (availability-checked):** Missouri State Bears: H.Belin IV, S.Locklear; Liberty Flames: D.Purdie, K.Davis — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401871063) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/flames-bears-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/flames-bears-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/flames-bears-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/flames-bears-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/flames-bears-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401871063) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=37.21533&longitude=-93.29824&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Georgia Tech Yellow Jackets (3-8) at #1 Georgia Bulldogs (10-1)
- **When/where:** Sat Nov 28, 12:30 PT (2026-11-28T20:30Z) — Sanford Stadium, Athens, GA
- **Pick:** Georgia Bulldogs
- **Predicted score:** Georgia Bulldogs 45.5, Georgia Tech Yellow Jackets 10 — arithmetic: margin_home = -line = 35.5; home = (total + margin)/2 = (55.5 + 35.5)/2 = 45.5; away = (total - margin)/2 = (55.5 - 35.5)/2 = 10
- **Line (DraftKings, labeled close at pull; pre-kickoff):** UGA -35.5, total 55.5
- **Power ratings (TeamRankings):** Predictive: GT -0.3 (#78), UGA 34.1 (#1); Last 5: GT -5.0 (#94), UGA 37.5 (#2); Home: GT -3.5 (#93), UGA 30.4 (#3); Away: GT 1.1 (#66), UGA 43.2 (#1)
- **Play metrics Georgia Bulldogs** (self-computed from ESPN play-by-play): adj EPA/play +0.085, adj success rate +0.086, adj explosiveness +0.037, raw SR 0.379, raw explosive 0.139, ypp 6.87, TO lost/gm 0.7, avg drive start own 32.3 yd, opp forced to own 72.8 yd (668 plays)
- **Play metrics Georgia Tech Yellow Jackets** (self-computed from ESPN play-by-play): adj EPA/play -0.028, adj success rate +0.015, adj explosiveness +0.018, raw SR 0.312, raw explosive 0.129, ypp 5.77, TO lost/gm 1.4, avg drive start own 27.4 yd, opp forced to own 67.6 yd (690 plays)
- **Turnover margin/gm (TeamRankings):** Georgia Tech -1.0, Georgia +0.9
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Georgia Tech Yellow Jackets 7 days (last 2026-11-21), Georgia Bulldogs 6 days (last 2026-11-22)
- **Travel (miles):** Georgia Tech Yellow Jackets 59, Georgia Bulldogs 0
- **Wind:** max sustained 16.3 km/h (10 mph), gusts 43.2 km/h (27 mph); temp 39.6-60.6F, precip 0% (open-meteo @ venue 33.96095,-83.37794, 2026-11-28)
- **Key players (availability-checked):** Georgia Bulldogs: G.Stockton, N.Frazier; Georgia Tech Yellow Jackets: A.Mendoza, J.Haynes — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856760) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/yellow-jackets-bulldogs-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/yellow-jackets-bulldogs-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/yellow-jackets-bulldogs-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/yellow-jackets-bulldogs-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/yellow-jackets-bulldogs-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856760) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=33.96095&longitude=-83.37794&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #15 USC Trojans (8-3) at #10 UCLA Bruins (10-1)
- **When/where:** Sat Nov 28, 12:30 PT (2026-11-28T20:30Z) — Rose Bowl, Pasadena, CA
- **Pick:** USC Trojans
- **Predicted score:** UCLA Bruins 19.25, USC Trojans 26.25 — arithmetic: margin_home = -line = -7; home = (total + margin)/2 = (45.5 + -7)/2 = 19.25; away = (total - margin)/2 = (45.5 - -7)/2 = 26.25
- **Line (DraftKings, labeled close at pull; pre-kickoff):** USC -7, total 45.5
- **Power ratings (TeamRankings):** Predictive: USC 15.9 (#22), UCLA 18.1 (#17); Last 5: USC 16.4 (#22), UCLA 15.9 (#24); Home: USC 17.4 (#23), UCLA 15.2 (#27); Away: USC 10.2 (#40), UCLA 27.2 (#7)
- **Play metrics UCLA Bruins** (self-computed from ESPN play-by-play): adj EPA/play +0.009, adj success rate +0.037, adj explosiveness +0.021, raw SR 0.308, raw explosive 0.113, ypp 5.76, TO lost/gm 1.6, avg drive start own 34.7 yd, opp forced to own 72.8 yd (708 plays)
- **Play metrics USC Trojans** (self-computed from ESPN play-by-play): adj EPA/play +0.080, adj success rate +0.050, adj explosiveness +0.004, raw SR 0.363, raw explosive 0.118, ypp 6.11, TO lost/gm 1.0, avg drive start own 29.1 yd, opp forced to own 72.7 yd (735 plays)
- **Turnover margin/gm (TeamRankings):** USC -0.1, UCLA +1.3
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** USC Trojans 7 days (last 2026-11-21), UCLA Bruins 7 days (last 2026-11-21)
- **Travel (miles):** USC Trojans 12, UCLA Bruins 0
- **Wind:** max sustained 8.4 km/h (5 mph), gusts 8.6 km/h (5 mph); temp 63.3-73.4F, precip 0% (open-meteo @ venue 34.14778,-118.14452, 2026-11-28)
- **Key players (availability-checked):** UCLA Bruins: T.Dieffenbach, W.Knight; USC Trojans: J.Maiava, K.Miller — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858543) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/trojans-bruins-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/trojans-bruins-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/trojans-bruins-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/trojans-bruins-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/trojans-bruins-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858543) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=34.14778&longitude=-118.14452&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Cincinnati Bearcats (6-5) at #11 BYU Cougars (9-2)
- **When/where:** Sat Nov 28, 12:30 PT (2026-11-28T20:30Z) — LaVell Edwards Stadium, Provo, UT
- **Pick:** BYU Cougars
- **Predicted score:** BYU Cougars 36, Cincinnati Bearcats 20.5 — arithmetic: margin_home = -line = 15.5; home = (total + margin)/2 = (56.5 + 15.5)/2 = 36; away = (total - margin)/2 = (56.5 - 15.5)/2 = 20.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** BYU -15.5, total 56.5
- **Power ratings (TeamRankings):** Predictive: CIN 3.4 (#65), BYU 17.4 (#19); Last 5: CIN 3.7 (#61), BYU 15.2 (#27); Home: CIN 11.1 (#42), BYU 22.8 (#13); Away: CIN -4.0 (#83), BYU 11.9 (#38)
- **Play metrics BYU Cougars** (self-computed from ESPN play-by-play): adj EPA/play +0.039, adj success rate +0.036, adj explosiveness +0.009, raw SR 0.336, raw explosive 0.116, ypp 5.81, TO lost/gm 1.1, avg drive start own 31.2 yd, opp forced to own 70.9 yd (697 plays)
- **Play metrics Cincinnati Bearcats** (self-computed from ESPN play-by-play): adj EPA/play +0.141, adj success rate +0.030, adj explosiveness +0.004, raw SR 0.348, raw explosive 0.120, ypp 6.56, TO lost/gm 0.6, avg drive start own 28.7 yd, opp forced to own 73.6 yd (724 plays)
- **Turnover margin/gm (TeamRankings):** Cincinnati +0.6, BYU -0.4
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Cincinnati Bearcats 7 days (last 2026-11-21), BYU Cougars 7 days (last 2026-11-21)
- **Travel (miles):** Cincinnati Bearcats 1443, BYU Cougars 0
- **Wind:** max sustained 6.9 km/h (4 mph), gusts 13 km/h (8 mph); temp 43.5-53.4F, precip 38% (open-meteo @ venue 40.23384,-111.65853, 2026-11-28)
- **Key players (availability-checked):** BYU Cougars: B.Bachmeier, L.Martin; Cincinnati Bearcats: J.French IV, C.Tabb — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856876) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/bearcats-cougars-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/bearcats-cougars-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/bearcats-cougars-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/bearcats-cougars-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/bearcats-cougars-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856876) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=40.23384&longitude=-111.65853&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Duke Blue Devils (7-4) at #8 Wake Forest Demon Deacons (10-1)
- **When/where:** Sat Nov 28, 12:30 PT (2026-11-28T20:30Z) — Allegacy Federal Credit Union Stadium, Winston-Salem, NC
- **Pick:** Wake Forest Demon Deacons
- **Predicted score:** Wake Forest Demon Deacons 35, Duke Blue Devils 20.5 — arithmetic: margin_home = -line = 14.5; home = (total + margin)/2 = (55.5 + 14.5)/2 = 35; away = (total - margin)/2 = (55.5 - 14.5)/2 = 20.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** WAKE -14.5, total 55.5
- **Power ratings (TeamRankings):** Predictive: DUKE 13.5 (#29), WAKE 23.7 (#10); Last 5: DUKE 22.5 (#12), WAKE 39.4 (#1); Home: DUKE 14.1 (#33), WAKE 29.4 (#5); Away: DUKE 18.6 (#20), WAKE 28.3 (#5)
- **Play metrics Wake Forest Demon Deacons** (self-computed from ESPN play-by-play): adj EPA/play +0.156, adj success rate +0.092, adj explosiveness +0.049, raw SR 0.380, raw explosive 0.151, ypp 6.95, TO lost/gm 0.4, avg drive start own 31.6 yd, opp forced to own 73.6 yd (723 plays)
- **Play metrics Duke Blue Devils** (self-computed from ESPN play-by-play): adj EPA/play +0.065, adj success rate +0.030, adj explosiveness +0.017, raw SR 0.312, raw explosive 0.121, ypp 5.82, TO lost/gm 0.6, avg drive start own 29.2 yd, opp forced to own 74.4 yd (718 plays)
- **Turnover margin/gm (TeamRankings):** Duke +0.4, Wake Forest +0.6
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Duke Blue Devils 7 days (last 2026-11-21), Wake Forest Demon Deacons 7 days (last 2026-11-21)
- **Travel (miles):** Duke Blue Devils 74, Wake Forest Demon Deacons 0
- **Wind:** max sustained 15.2 km/h (9 mph), gusts 46.1 km/h (29 mph); temp 39.4-57F, precip 0% (open-meteo @ venue 36.09986,-80.24422, 2026-11-28)
- **Key players (availability-checked):** Wake Forest Demon Deacons: G.Lopez, T.Clark; Duke Blue Devils: W.Eget, N.Sheppard — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858312) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/blue-devils-demon-deacons-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/blue-devils-demon-deacons-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/blue-devils-demon-deacons-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/blue-devils-demon-deacons-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/blue-devils-demon-deacons-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858312) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=36.09986&longitude=-80.24422&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #19 Oklahoma Sooners (7-4) at #24 Missouri Tigers (7-4)
- **When/where:** Sat Nov 28, 13:15 PT (2026-11-28T21:15Z) — Memorial Stadium, Columbia, MO
- **Pick:** Missouri Tigers
- **Predicted score:** Missouri Tigers 22, Oklahoma Sooners 19.5 — arithmetic: margin_home = -line = 2.5; home = (total + margin)/2 = (41.5 + 2.5)/2 = 22; away = (total - margin)/2 = (41.5 - 2.5)/2 = 19.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** MIZ -2.5, total 41.5
- **Power ratings (TeamRankings):** Predictive: OKLA 18.1 (#18), MIZZ 16.5 (#21); Last 5: OKLA 20.9 (#14), MIZZ 14.7 (#30); Home: OKLA 14.6 (#32), MIZZ 19.4 (#17); Away: OKLA 16.9 (#24), MIZZ 13.9 (#33)
- **Play metrics Missouri Tigers** (self-computed from ESPN play-by-play): adj EPA/play +0.024, adj success rate +0.002, adj explosiveness +0.018, raw SR 0.302, raw explosive 0.118, ypp 5.82, TO lost/gm 0.7, avg drive start own 31.5 yd, opp forced to own 71.9 yd (711 plays)
- **Play metrics Oklahoma Sooners** (self-computed from ESPN play-by-play): adj EPA/play -0.021, adj success rate -0.007, adj explosiveness -0.012, raw SR 0.279, raw explosive 0.085, ypp 5.22, TO lost/gm 1.3, avg drive start own 27.2 yd, opp forced to own 69.4 yd (648 plays)
- **Turnover margin/gm (TeamRankings):** Oklahoma -0.4, Missouri +1.2
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Oklahoma Sooners 7 days (last 2026-11-21), Missouri Tigers 6 days (last 2026-11-22)
- **Travel (miles):** Oklahoma Sooners 381, Missouri Tigers 0
- **Wind:** max sustained 20 km/h (12 mph), gusts 50.4 km/h (31 mph); temp 36.7-57.6F, precip 8% (open-meteo @ venue 38.95171,-92.33407, 2026-11-28)
- **Key players (availability-checked):** Missouri Tigers: A.Simmons, J.Roberts; Oklahoma Sooners: J.Mateer, L.Avant — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856763) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/sooners-tigers-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/sooners-tigers-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/sooners-tigers-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/sooners-tigers-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/sooners-tigers-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856763) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=38.95171&longitude=-92.33407&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #22 Boise State Broncos (9-2) at Colorado State Rams (3-8)
- **When/where:** Sat Nov 28, 15:00 PT (2026-11-28T23:00Z) — Canvas Stadium, Fort Collins, CO
- **Pick:** Boise State Broncos
- **Predicted score:** Colorado State Rams 27.75, Boise State Broncos 48.75 — arithmetic: margin_home = -line = -21; home = (total + margin)/2 = (76.5 + -21)/2 = 27.75; away = (total - margin)/2 = (76.5 - -21)/2 = 48.75
- **Line (DraftKings, labeled close at pull; pre-kickoff):** BOIS -21, total 76.5
- **Power ratings (TeamRankings):** Predictive: BSU 10.1 (#38), CSU -14.1 (#121); Last 5: BSU 7.4 (#51), CSU -21.2 (#130); Home: BSU 3.9 (#69), CSU -7.1 (#101); Away: BSU 18.4 (#21), CSU -25.6 (#135)
- **Play metrics Colorado State Rams** (self-computed from ESPN play-by-play): adj EPA/play +0.100, adj success rate -0.006, adj explosiveness +0.003, raw SR 0.322, raw explosive 0.119, ypp 6.16, TO lost/gm 1.0, avg drive start own 29.3 yd, opp forced to own 69.6 yd (723 plays)
- **Play metrics Boise State Broncos** (self-computed from ESPN play-by-play): adj EPA/play +0.122, adj success rate +0.065, adj explosiveness -0.001, raw SR 0.365, raw explosive 0.111, ypp 5.87, TO lost/gm 0.6, avg drive start own 26.8 yd, opp forced to own 72.2 yd (756 plays)
- **Turnover margin/gm (TeamRankings):** Boise St +0.1, Colorado St +0.1
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Boise State Broncos 6 days (last 2026-11-22), Colorado State Rams 6 days (last 2026-11-22)
- **Travel (miles):** Boise State Broncos 606, Colorado State Rams 0
- **Wind:** max sustained 13.9 km/h (9 mph), gusts 56.9 km/h (35 mph); temp 43.5-60.3F, precip 21% (open-meteo @ venue 40.58526,-105.08442, 2026-11-28)
- **Key players (availability-checked):** Colorado State Rams: H.Hejny, K.Farrar; Boise State Broncos: M.Madsen, D.Riley — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401860926) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/broncos-rams-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/broncos-rams-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/broncos-rams-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/broncos-rams-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/broncos-rams-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401860926) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=40.58526&longitude=-105.08442&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Purdue Boilermakers (3-8) at #12 Indiana Hoosiers (9-2)
- **When/where:** Sat Nov 28, 16:00 PT (2026-11-29T00:00Z) — Memorial Stadium (Bloomington, IN), Bloomington, IN
- **Pick:** Indiana Hoosiers
- **Predicted score:** Indiana Hoosiers 37.5, Purdue Boilermakers 15 — arithmetic: margin_home = -line = 22.5; home = (total + margin)/2 = (52.5 + 22.5)/2 = 37.5; away = (total - margin)/2 = (52.5 - 22.5)/2 = 15
- **Line (DraftKings, labeled close at pull; pre-kickoff):** IU -22.5, total 52.5
- **Power ratings (TeamRankings):** Predictive: PUR 1.9 (#72), IND 22.5 (#11); Last 5: PUR -5.7 (#97), IND 17.3 (#18); Home: PUR 0.7 (#78), IND 21.1 (#15); Away: PUR 7.0 (#50), IND 21.0 (#15)
- **Play metrics Indiana Hoosiers** (self-computed from ESPN play-by-play): adj EPA/play +0.113, adj success rate +0.048, adj explosiveness +0.036, raw SR 0.330, raw explosive 0.137, ypp 6.56, TO lost/gm 0.5, avg drive start own 31.9 yd, opp forced to own 72.4 yd (663 plays)
- **Play metrics Purdue Boilermakers** (self-computed from ESPN play-by-play): adj EPA/play +0.047, adj success rate +0.012, adj explosiveness +0.002, raw SR 0.318, raw explosive 0.117, ypp 5.70, TO lost/gm 0.9, avg drive start own 28.3 yd, opp forced to own 71.6 yd (702 plays)
- **Turnover margin/gm (TeamRankings):** Purdue -0.1, Indiana +0.6
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Purdue Boilermakers 8 days (last 2026-11-21), Indiana Hoosiers 8 days (last 2026-11-21)
- **Travel (miles):** Purdue Boilermakers 89, Indiana Hoosiers 0
- **Wind:** max sustained 21.3 km/h (13 mph), gusts 56.9 km/h (35 mph); temp 32.7-49.1F, precip 8% (open-meteo @ venue 39.16533,-86.52639, 2026-11-28)
- **Key players (availability-checked):** Indiana Hoosiers: J.Hoover, L.Beebe Jr.; Purdue Boilermakers: R.Browne, F.Ijeboi — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858538) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/boilermakers-hoosiers-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/boilermakers-hoosiers-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/boilermakers-hoosiers-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/boilermakers-hoosiers-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/boilermakers-hoosiers-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858538) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=39.16533&longitude=-86.52639&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### #7 Tennessee Volunteers (9-2) at Vanderbilt Commodores (4-7)
- **When/where:** Sat Nov 28, 16:00 PT (2026-11-29T00:00Z) — FirstBank Stadium, Nashville, TN
- **Pick:** Tennessee Volunteers
- **Predicted score:** Vanderbilt Commodores 15, Tennessee Volunteers 28.5 — arithmetic: margin_home = -line = -13.5; home = (total + margin)/2 = (43.5 + -13.5)/2 = 15; away = (total - margin)/2 = (43.5 - -13.5)/2 = 28.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** TENN -13.5, total 43.5
- **Power ratings (TeamRankings):** Predictive: TENN 24.2 (#9), VAN 4.0 (#62); Last 5: TENN 32.1 (#4), VAN 5.0 (#57); Home: TENN 28.6 (#6), VAN -2.7 (#88); Away: TENN 21.0 (#14), VAN 9.1 (#44)
- **Play metrics Vanderbilt Commodores** (self-computed from ESPN play-by-play): adj EPA/play -0.030, adj success rate -0.020, adj explosiveness -0.010, raw SR 0.294, raw explosive 0.105, ypp 5.15, TO lost/gm 1.0, avg drive start own 29.9 yd, opp forced to own 72.5 yd (686 plays)
- **Play metrics Tennessee Volunteers** (self-computed from ESPN play-by-play): adj EPA/play +0.042, adj success rate +0.014, adj explosiveness +0.003, raw SR 0.314, raw explosive 0.106, ypp 5.61, TO lost/gm 0.9, avg drive start own 32.5 yd, opp forced to own 72.3 yd (736 plays)
- **Turnover margin/gm (TeamRankings):** Tennessee +1.0, Vanderbilt -0.6
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Tennessee Volunteers 8 days (last 2026-11-21), Vanderbilt Commodores 8 days (last 2026-11-21)
- **Travel (miles):** Tennessee Volunteers 161, Vanderbilt Commodores 0
- **Wind:** max sustained 19.6 km/h (12 mph), gusts 47.5 km/h (30 mph); temp 37.8-57.4F, precip 1% (open-meteo @ venue 36.16589,-86.78444, 2026-11-28)
- **Key players (availability-checked):** Vanderbilt Commodores: J.Curtis, S.Alexander; Tennessee Volunteers: D.Bishop, G.MacIntyre — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856765) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/volunteers-commodores-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/volunteers-commodores-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/volunteers-commodores-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/volunteers-commodores-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/volunteers-commodores-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856765) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=36.16589&longitude=-86.78444&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Auburn Tigers (7-4) at #6 Alabama Crimson Tide (9-2)
- **When/where:** Sat Nov 28, 16:30 PT (2026-11-29T00:30Z) — Bryant-Denny Stadium, Tuscaloosa, AL
- **Pick:** Alabama Crimson Tide
- **Predicted score:** Alabama Crimson Tide 32.5, Auburn Tigers 17 — arithmetic: margin_home = -line = 15.5; home = (total + margin)/2 = (49.5 + 15.5)/2 = 32.5; away = (total - margin)/2 = (49.5 - 15.5)/2 = 17
- **Line (DraftKings, labeled close at pull; pre-kickoff):** ALA -15.5, total 49.5
- **Power ratings (TeamRankings):** Predictive: AUB 14.3 (#27), ALA 28.0 (#4); Last 5: AUB 11.3 (#41), ALA 24.4 (#9); Home: AUB 8.8 (#50), ALA 26.8 (#7); Away: AUB 22.9 (#11), ALA 32.8 (#2)
- **Play metrics Alabama Crimson Tide** (self-computed from ESPN play-by-play): adj EPA/play +0.055, adj success rate +0.061, adj explosiveness +0.030, raw SR 0.347, raw explosive 0.133, ypp 6.17, TO lost/gm 0.9, avg drive start own 32.9 yd, opp forced to own 73.7 yd (682 plays)
- **Play metrics Auburn Tigers** (self-computed from ESPN play-by-play): adj EPA/play +0.007, adj success rate +0.014, adj explosiveness +0.028, raw SR 0.321, raw explosive 0.133, ypp 5.62, TO lost/gm 1.2, avg drive start own 29.3 yd, opp forced to own 71.5 yd (744 plays)
- **Turnover margin/gm (TeamRankings):** Auburn +0.6, Alabama +0.7
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Auburn Tigers 8 days (last 2026-11-21), Alabama Crimson Tide 8 days (last 2026-11-21)
- **Travel (miles):** Auburn Tigers 127, Alabama Crimson Tide 0
- **Wind:** max sustained 11 km/h (7 mph), gusts 26.3 km/h (16 mph); temp 40.5-61.9F, precip 1% (open-meteo @ venue 33.20984,-87.56917, 2026-11-28)
- **Key players (availability-checked):** Alabama Crimson Tide: K.Russell, D.Hill; Auburn Tigers: B.Brown, J.Cobb — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856757) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/tigers-crimson-tide-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/tigers-crimson-tide-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/tigers-crimson-tide-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/tigers-crimson-tide-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/tigers-crimson-tide-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856757) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=33.20984&longitude=-87.56917&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Washington Huskies (7-4) at #14 Oregon Ducks (8-3)
- **When/where:** Sat Nov 28, 16:30 PT (2026-11-29T00:30Z) — Autzen Stadium, Eugene, OR
- **Pick:** Oregon Ducks
- **Predicted score:** Oregon Ducks 32.25, Washington Huskies 18.25 — arithmetic: margin_home = -line = 14; home = (total + margin)/2 = (50.5 + 14)/2 = 32.25; away = (total - margin)/2 = (50.5 - 14)/2 = 18.25
- **Line (DraftKings, labeled close at pull; pre-kickoff):** ORE -14, total 50.5
- **Power ratings (TeamRankings):** Predictive: WASH 11.1 (#36), ORE 25.5 (#8); Last 5: WASH 16.9 (#21), ORE 27.0 (#5); Home: WASH 5.3 (#61), ORE 23.3 (#12); Away: WASH 17.2 (#23), ORE 25.6 (#8)
- **Play metrics Oregon Ducks** (self-computed from ESPN play-by-play): adj EPA/play +0.065, adj success rate +0.009, adj explosiveness +0.014, raw SR 0.312, raw explosive 0.121, ypp 5.84, TO lost/gm 0.9, avg drive start own 32.2 yd, opp forced to own 72.6 yd (749 plays)
- **Play metrics Washington Huskies** (self-computed from ESPN play-by-play): adj EPA/play -0.032, adj success rate +0.007, adj explosiveness +0.031, raw SR 0.307, raw explosive 0.135, ypp 5.60, TO lost/gm 0.8, avg drive start own 27.1 yd, opp forced to own 71.3 yd (684 plays)
- **Turnover margin/gm (TeamRankings):** Washington +0.4, Oregon +0.0
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Washington Huskies 8 days (last 2026-11-21), Oregon Ducks 8 days (last 2026-11-21)
- **Travel (miles):** Washington Huskies 251, Oregon Ducks 0
- **Wind:** max sustained 8 km/h (5 mph), gusts 9.7 km/h (6 mph); temp 54-59.5F, precip 30% (open-meteo @ venue 44.05207,-123.08675, 2026-11-28)
- **Key players (availability-checked):** Oregon Ducks: D.Raiola, D.Hill Jr; Washington Huskies: D.Williams Jr., E.Brown — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858541) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/huskies-ducks-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/huskies-ducks-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/huskies-ducks-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/huskies-ducks-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/huskies-ducks-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401858541) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=44.05207&longitude=-123.08675&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Arizona State Sun Devils (6-5) at #16 Arizona Wildcats (8-3)
- **When/where:** Sat Nov 28, 18:00 PT (2026-11-29T02:00Z) — Casino Del Sol Stadium, Tucson, AZ
- **Pick:** Arizona Wildcats
- **Predicted score:** Arizona Wildcats 31, Arizona State Sun Devils 22.5 — arithmetic: margin_home = -line = 8.5; home = (total + margin)/2 = (53.5 + 8.5)/2 = 31; away = (total - margin)/2 = (53.5 - 8.5)/2 = 22.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** ARIZ -8.5, total 53.5
- **Power ratings (TeamRankings):** Predictive: ASU 6.8 (#50), ARIZ 14.2 (#28); Last 5: ASU 13.4 (#33), ARIZ 18.3 (#15); Home: ASU 5.9 (#59), ARIZ 15.9 (#26); Away: ASU 4.8 (#55), ARIZ 14.9 (#29)
- **Play metrics Arizona Wildcats** (self-computed from ESPN play-by-play): adj EPA/play +0.094, adj success rate +0.027, adj explosiveness +0.001, raw SR 0.325, raw explosive 0.110, ypp 5.80, TO lost/gm 0.7, avg drive start own 29.2 yd, opp forced to own 71.2 yd (747 plays)
- **Play metrics Arizona State Sun Devils** (self-computed from ESPN play-by-play): adj EPA/play +0.067, adj success rate +0.007, adj explosiveness -0.003, raw SR 0.298, raw explosive 0.098, ypp 5.35, TO lost/gm 0.6, avg drive start own 29.5 yd, opp forced to own 69.2 yd (748 plays)
- **Turnover margin/gm (TeamRankings):** Arizona St +0.0, Arizona +0.3
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Arizona State Sun Devils 7 days (last 2026-11-22), Arizona Wildcats 7 days (last 2026-11-22)
- **Travel (miles):** Arizona State Sun Devils 79, Arizona Wildcats 0
- **Wind:** max sustained 10.5 km/h (7 mph), gusts 10.4 km/h (6 mph); temp 61.3-73F, precip 0% (open-meteo @ venue 32.22174,-110.92648, 2026-11-28)
- **Key players (availability-checked):** Arizona Wildcats: N.Fifita, K.Reescano; Arizona State Sun Devils: C.Boley, J.Fette — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856873) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/sun-devils-wildcats-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/sun-devils-wildcats-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/sun-devils-wildcats-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/sun-devils-wildcats-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/sun-devils-wildcats-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856873) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=32.22174&longitude=-110.92648&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

### Baylor Bears (6-5) at #17 Houston Cougars (8-3)
- **When/where:** Sat Nov 28, 18:30 PT (2026-11-29T02:30Z) — TDECU Stadium, Houston, TX
- **Pick:** Houston Cougars
- **Predicted score:** Houston Cougars 30, Baylor Bears 25.5 — arithmetic: margin_home = -line = 4.5; home = (total + margin)/2 = (55.5 + 4.5)/2 = 30; away = (total - margin)/2 = (55.5 - 4.5)/2 = 25.5
- **Line (DraftKings, labeled close at pull; pre-kickoff):** HOU -4.5, total 55.5
- **Power ratings (TeamRankings):** Predictive: BAY 13.1 (#32), HOU 14.6 (#25); Last 5: BAY 14.4 (#31), HOU 8.6 (#47); Home: BAY 9.2 (#48), HOU 17.4 (#22); Away: BAY 24.7 (#9), HOU 13.8 (#34)
- **Play metrics Houston Cougars** (self-computed from ESPN play-by-play): adj EPA/play +0.113, adj success rate +0.072, adj explosiveness +0.015, raw SR 0.378, raw explosive 0.121, ypp 6.39, TO lost/gm 0.6, avg drive start own 31.8 yd, opp forced to own 75.3 yd (761 plays)
- **Play metrics Baylor Bears** (self-computed from ESPN play-by-play): adj EPA/play +0.045, adj success rate -0.004, adj explosiveness +0.011, raw SR 0.282, raw explosive 0.117, ypp 5.15, TO lost/gm 1.0, avg drive start own 32.2 yd, opp forced to own 72.4 yd (797 plays)
- **Turnover margin/gm (TeamRankings):** Baylor +0.9, Houston +0.3
- **Home field:** venue above; home/away power splits above; ESPN-labeled conditions: n/a
- **Rest:** Baylor Bears 8 days (last 2026-11-21), Houston Cougars 8 days (last 2026-11-21)
- **Travel (miles):** Baylor Bears 164, Houston Cougars 0
- **Wind:** max sustained 14.3 km/h (9 mph), gusts 35.3 km/h (22 mph); temp 55.4-68.9F, precip 1% (open-meteo @ venue 29.76328,-95.36327, 2026-11-28)
- **Key players (availability-checked):** Houston Cougars: C.Weigman, M.Hughes; Baylor Bears: D.Lagway, D.Pendergrass — every name taken from this season's ESPN play-by-play (recent ball handlers) and cross-checked against the ESPN league injuries feed + TeamRankings injury page pulled 2026-11-25: no injury-report entry for any named player
- **Sources (16, all pulled 2026-11-25):**
  1. [ESPN scoreboard API (event list, records, venue)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261128) — pulled 2026-11-25
  2. [ESPN summary API (pickcenter spread/total labeled close)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856874) — pulled 2026-11-25
  3. [TeamRankings power ratings](https://www.teamrankings.com/college-football/matchup/bears-cougars-week-13-2026/power-ratings) — pulled 2026-11-25
  4. [TeamRankings matchup efficiency (points/play, yards/play, opp-adjusted)](https://www.teamrankings.com/college-football/matchup/bears-cougars-week-13-2026/efficiency) — pulled 2026-11-25
  5. [TeamRankings matchup stats (turnovers, downs, scoring splits)](https://www.teamrankings.com/college-football/matchup/bears-cougars-week-13-2026/stats) — pulled 2026-11-25
  6. [TeamRankings travel/distance report](https://www.teamrankings.com/college-football/matchup/bears-cougars-week-13-2026/travel) — pulled 2026-11-25
  7. [TeamRankings injuries (named players)](https://www.teamrankings.com/college-football/matchup/bears-cougars-week-13-2026/injuries) — pulled 2026-11-25
  8. [ESPN league injuries API feed (availability check)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries) — pulled 2026-11-25
  9. [ESPN play-by-play summary API (self-computed EPA/SR/explosive/field-position, see pbmetrics.py)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=401856874) — pulled 2026-11-25
  10. [ESPN scoreboard API (Week 12 results -> rest days)](https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261119) — pulled 2026-11-25
  11. [open-meteo forecast API (wind, gusts, temp, precip)](https://api.open-meteo.com/v1/forecast?latitude=29.76328&longitude=-95.36327&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&start_date=2026-11-27&end_date=2026-11-29) — pulled 2026-11-25
  12. [TeamRankings turnover margin per game (league table)](https://www.teamrankings.com/college-football/stat/turnover-margin-per-game) — pulled 2026-11-25
  13. [TeamRankings yards per play (league table)](https://www.teamrankings.com/college-football/stat/yards-per-play) — pulled 2026-11-25
  14. [TeamRankings points-per-play margin (league table)](https://www.teamrankings.com/college-football/stat/points-per-play-margin) — pulled 2026-11-25
  15. [TeamRankings red-zone scoring pct (league table)](https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct) — pulled 2026-11-25
  16. [TeamRankings third-down conversion pct (league table)](https://www.teamrankings.com/college-football/stat/third-down-conversion-pct) — pulled 2026-11-25

---

Reproduce (no API keys; raw pulls ship in `raw/`): from the repo root run `python3 src/pbmetrics.py && python3 src/extract.py && python3 src/build_filing.py --out src/FILING.md`; `src/pull.sh` refreshes the raw pulls. Unit tests: `cd src && python3 -m pytest -q`.
