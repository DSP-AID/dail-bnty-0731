#!/bin/bash
# Re-pull every public dataset used by the filing (no API keys needed).
# The repo already ships raw/ as pulled 2026-11-25, so this is only for
# re-verifying freshness. Run from the task root (the dir containing src/ raw/).
set -u
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
mkdir -p raw/espn/pb raw/tr raw/weather

# 1. TeamRankings matchup pages for the 24 slate games (overview, travel,
#    injuries, power-ratings, efficiency, stats subpages)
slugs="longhorns-aggies golden-gophers-badgers cornhuskers-hawkeyes bulldogs-rebels gators-seminoles mountaineers-utes eagles-hurricanes cardinals-wildcats flames-bears bearcats-cougars blue-devils-demon-deacons yellow-jackets-bulldogs sooners-tigers broncos-rams boilermakers-hoosiers volunteers-commodores tigers-crimson-tide wolverines-buckeyes huskies-ducks sun-devils-wildcats bears-cougars trojans-bruins fighting-irish-orange"
for s in $slugs; do
  for sub in "" travel injuries power-ratings efficiency stats; do
    f="raw/tr/${s}-${sub:-overview}.html"
    [ -s "$f" ] || curl -sS --compressed -A "$UA" "https://www.teamrankings.com/college-football/matchup/${s}-week-13-2026/${sub}" -o "$f"
    sleep 0.5
  done
done

# 2. TeamRankings league stat pages
for u in turnover-margin-per-game yards-per-play points-per-play-margin red-zone-scoring-pct third-down-conversion-pct net-punting-average field-position-rank; do
  f="raw/tr/stat_${u}.html"
  [ -s "$f" ] || curl -sS --compressed -A "$UA" "https://www.teamrankings.com/college-football/stat/${u}" -o "$f"
  sleep 0.5
done

# 3. ESPN scoreboards: full season window + filing week
for d in $(python3 -c "
from datetime import date, timedelta
d = date(2026, 8, 29)
while d <= date(2026, 11, 23):
    print(d.strftime('%Y%m%d')); d += timedelta(days=1)"); do
  f="raw/espn/sb_${d}.json"
  [ -s "$f" ] || curl -sS --compressed "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=${d}" -o "$f"
  sleep 0.15
done

# 4. ESPN game summaries (odds w/ close lines, weather labels) for slate events
for e in $(python3 -c "import json;print(' '.join(g['event'] for g in json.load(open('src/data/slate.json'))))"); do
  f="raw/espn/sum_${e}.json"
  [ -s "$f" ] || curl -sS --compressed "https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=${e}" -o "$f"
  sleep 0.3
done

# 5. ESPN league injuries feed (availability check) + current AP Top 25
[ -s raw/espn/injuries.json ] || curl -sS --compressed "https://site.api.espn.com/apis/site/v2/sports/football/college-football/injuries" -o raw/espn/injuries.json
[ -s src/data/ap_poll_w13.json ] || curl -sS --compressed "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2026/types/2/weeks/13/rankings/1" -o src/data/ap_poll_w13.json

# 6. Play-by-play summary JSON for every completed game of every slate team
python3 - <<'PY' > /tmp/pb_events.txt
import json, glob
slate = set()
for g in json.load(open('src/data/slate.json')):
    slate.add(g['away_id']); slate.add(g['home_id'])
evs = []
for f in glob.glob('raw/espn/sb_*.json'):
    try: d = json.load(open(f))
    except Exception: continue
    for e in d.get('events', []):
        comp = (e.get('competitions') or [{}])[0]
        if not ((comp.get('status') or {}).get('type', {})).get('completed'): continue
        tids = {str((c.get('team') or {}).get('id', '')) for c in comp.get('competitors', [])}
        if tids & slate: evs.append(e['id'])
print('\n'.join(sorted(set(evs))))
PY
while read -r eid; do
  f="raw/espn/pb/pb_${eid}.json"
  [ -s "$f" ] || curl -sS --compressed "https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=${eid}&end=boxscore" -o "$f"
  sleep 0.15
done < /tmp/pb_events.txt

# 7. open-meteo geocoding + venue weather forecast for kickoff window
python3 - <<'PY' > /tmp/cities.txt
import json
seen = set()
for g in json.load(open('src/data/slate.json')):
    c = f"{g['city']}, {g['state']}"
    if c not in seen: seen.add(c); print(c)
PY
while IFS= read -r city; do
  k=$(echo "$city" | tr ' ,.' '___')
  g="raw/weather/geo_${k}.json"
  [ -s "$g" ] || curl -sS "https://geocoding-api.open-meteo.com/v1/search?name=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$city")&count=1&language=en&format=json" -o "$g"
  sleep 0.2
done < /tmp/cities.txt
while IFS= read -r city; do
  k=$(echo "$city" | tr ' ,.' '___')
  g="raw/weather/geo_${k}.json"
  lat=$(python3 -c "import json;d=json.load(open('$g'));print((d.get('results') or [{}])[0].get('latitude',''))")
  lon=$(python3 -c "import json;d=json.load(open('$g'));print((d.get('results') or [{}])[0].get('longitude',''))")
  tz=$(python3 -c "import json;d=json.load(open('$g'));print((d.get('results') or [{}])[0].get('timezone','America/Chicago'))")
  [ -n "$lat" ] || continue
  w="raw/weather/wx_${k}.json"
  [ -s "$w" ] || curl -sS "https://api.open-meteo.com/v1/forecast?latitude=$lat&longitude=$lon&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,cloud_cover_mean&timezone=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$tz")&start_date=2026-11-27&end_date=2026-11-29" -o "$w"
  sleep 0.2
done < /tmp/cities.txt
echo DONE
