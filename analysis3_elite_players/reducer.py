#!/usr/bin/python
import sys

current_year = None
current_player_id = None
current_pts = 0
current_ast = 0
current_games = 0
count = 0

for line in sys.stdin:
    key, values = line.strip().split("\t")
    year, player_id = key.split(",")
    pts, ast, games, value = map(float, values.split(","))

    if year == current_year and player_id == current_player_id:
        current_pts += pts
        current_ast += ast
        current_games += games
    else:
        if current_player_id is not None and current_games > 0:
            avg_pts = current_pts / current_games
            avg_ast = current_ast / current_games
            if avg_pts >= 20 or avg_ast >= 10:
                    count += value
        if year != current_year and current_year is not None:
            print(f"{current_year}\t{count}")
            count = 0

        current_year = year
        current_player_id = player_id
        current_pts = pts
        current_ast = ast
        current_games = games

if current_player_id is not None and current_games > 0:
    avg_pts = current_pts / current_games
    avg_ast = current_ast / current_games
    if avg_pts >= 20 or avg_ast >= 10:
        count += value

if current_year:
    print(f"{current_year}\t{count}")
