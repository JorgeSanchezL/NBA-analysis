#!/usr/bin/python
import sys

current_year = None
total_pts = total_ast = total_trb = count = 0

for line in sys.stdin:
    year, values = line.strip().split("\t")
    pts, ast, trb, n = map(float, values.split(","))

    if current_year == year:
        total_pts += pts
        total_ast += ast
        total_trb += trb
        count += 1
    else:
        if current_year:
            avg_pts = total_pts / count
            avg_ast = total_ast / count
            avg_trb = total_trb / count
            print(f"{current_year}\t{avg_pts:.2f},{avg_ast:.2f},{avg_trb:.2f}")
        current_year = year
        total_pts = pts
        total_ast = ast
        total_trb = trb
        count = 1

if current_year:
    avg_pts = total_pts / count
    avg_ast = total_ast / count
    avg_trb = total_trb / count
    print(f"{current_year}\t{avg_pts:.2f},{avg_ast:.2f},{avg_trb:.2f}")
