"""Unit tests for the Week 13 filing pipeline: extract.py + pbmetrics.py helpers."""
import json
import os

import pbmetrics as pbm
from extract import predict, season_records, table_rows, text_of

HERE = os.path.dirname(os.path.abspath(__file__))


def _play(down, dist, line_start, line_end, ttype="Rush", end_down=1, end_dist=10,
          a_s=0, h_s=0, text="#4 C.Joseph rush for 5 yards"):
    return {"start": {"down": down, "distance": dist, "yardLine": line_start,
                      "team": None},
            "end": {"down": end_down, "distance": end_dist, "yardLine": line_end},
            "type": {"text": ttype}, "text": text,
            "awayScore": a_s, "homeScore": h_s}


def _synth_game():
    """Home team '1' vs away team '2'. Home goal-line yardlines (ESPN convention)."""
    g = {"event": "t1", "tids": ["1", "2"], "home": "1", "drives": []}
    d1 = {"team": {"id": "1"}, "start": {"yardLine": 30}, "plays": []}
    p = _play(1, 10, 30, 50)                      # +20 gain: explosive + first down
    p["start"]["team"] = {"id": "1"}
    p2 = _play(1, 10, 50, 45, end_down=2, end_dist=15)   # -5 gain, fail
    p2["start"]["team"] = {"id": "1"}
    d1["plays"] = [p, p2]
    d2 = {"team": {"id": "2"}, "start": {"yardLine": 40}, "plays": []}
    p3 = _play(2, 7, 40, 35)                      # away gains 5 (absolute decreases)
    p3["start"]["team"] = {"id": "2"}
    d2["plays"] = [p3]
    g["drives"] = [d1, d2]
    return g


def test_ybin_dbin_bounds():
    assert pbm.ybin(1) == 0 and pbm.ybin(99) == 19 and pbm.ybin(-5) == 0
    assert pbm.dbin(3) == 0 and pbm.dbin(4) == 1 and pbm.dbin(8) == 2 and pbm.dbin(20) == 3


def test_prog_orientation():
    g = _synth_game()
    assert pbm.prog(g, "1", 30) == 30      # home: yardLine is already from own goal
    assert pbm.prog(g, "2", 30) == 70      # away: mirror


def test_season_stats_counts():
    g = _synth_game()
    ep = pbm.fit_ep([g])
    s = pbm.season_stats([g], ep)
    assert s["1"]["plays"] == 2
    assert s["1"]["success_rate"] == 0.5          # first play: +20 -> first down
    assert s["1"]["explosive_rate"] == 0.5        # >=15 yds once
    assert abs(s["1"]["ypp"] - 7.5) < 1e-9        # (20 + -5)/2
    assert s["2"]["ypp"] == 5.0                   # away orientation: 40->35 = +5
    assert s["1"]["turnovers_lost_per_game"] == 0.0
    assert s["1"]["field_pos_avg_start"] == 30.0
    assert s["2"]["field_pos_avg_start"] == 60.0  # own-goal conversion of yardLine 40


def test_opponent_adjust_symmetry():
    g = _synth_game()
    ep = pbm.fit_ep([g])
    s = pbm.season_stats([g], ep)
    adj = pbm.opponent_adjust(s, [g])
    # with two teams that only faced each other: adj_a == -adj_b
    assert abs(adj["1"]["adj_success_rate"] + adj["2"]["adj_success_rate"]) < 1e-9


def test_key_players_from_play_text():
    g = _synth_game()
    kp = pbm.key_players([g])
    assert kp["1"][0][0] == "C.Joseph"


def test_predict_arithmetic():
    p = predict(47.5, -14.0)
    assert p["margin_home"] == 14.0
    assert p["home_pts"] == 30.75 and p["away_pts"] == 16.75
    assert abs(p["home_pts"] + p["away_pts"] - 47.5) < 1e-9
    assert predict(None, -3) is None and predict(45, None) is None


def test_text_of_and_table_rows():
    assert text_of("<b>A&nbsp;B</b>") == "A B"
    rows = table_rows("<table><tr><th>x</th></tr><tr><td>a</td><td>1</td></tr></table>")
    assert ["a", "1"] in rows


def test_season_records(tmp_path):
    ev = {"events": [{"competitions": [{
        "status": {"type": {"completed": True}},
        "competitors": [{"team": {"id": "9"}, "winner": True},
                        {"team": {"id": "8"}}]}]}]}
    (tmp_path / "espn").mkdir()
    for i in range(2):
        (tmp_path / "espn" / f"sb_{i}.json").write_text(json.dumps(ev))
    assert season_records(str(tmp_path)) == {"9": "2-0", "8": "0-2"}
