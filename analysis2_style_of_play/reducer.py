#!/usr/bin/python
import sys

current_year = None
sum_3p = sum_fg_total = sum_mp = count = 0

for line in sys.stdin:
    year, values = line.strip().split("\t")
    three, fg_total, mp, n = map(float, values.split(","))

    if year == current_year:
        sum_3p += three
        sum_fg_total += fg_total
        sum_mp += mp
        count += 1
    else:
        if current_year:
            avg_3p = sum_3p / count
            avg_fg_total = sum_fg_total / count
            avg_mp = sum_mp / count
            three_pct = (sum_3p / sum_fg_total) * 100 if sum_fg_total > 0 else 0
            print(f"{current_year}\t{avg_3p:.2f},{avg_fg_total:.2f},{avg_mp:.2f},{three_pct:.2f}")
        
        current_year = year
        sum_3p = three
        sum_fg_total = fg_total
        sum_mp = mp
        count = 1

if current_year:
    avg_3p = sum_3p / count
    avg_fg_total = sum_fg_total / count
    avg_mp = sum_mp / count
    three_pct = (sum_3p / sum_fg_total) * 100 if sum_fg_total > 0 else 0
    print(f"{current_year}\t{avg_3p:.2f},{avg_fg_total:.2f},{avg_mp:.2f},{three_pct:.2f}")
