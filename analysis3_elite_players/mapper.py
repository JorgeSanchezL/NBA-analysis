#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)

for row in reader:
    try:
        year = row[1] if row[10] else None
        player_id = row[2] if row[2] else None
        pts = float(row[34]) if row[34] else 0
        ast = float(row[29]) if row[29] else 0
        games = float(row[10]) if row[10] else 0
        if games == 0:
            continue
        if year is not None and player_id is not None and pts is not None and ast is not None and games is not None:
            print(f"{year},{player_id}\t{pts},{ast},{games},1")
    except:
        continue
