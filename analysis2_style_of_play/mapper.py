#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header

for row in reader:
    # Check if the essential columns are available and valid
    try:
        year = row[1] if row[1] else None
        three_made = float(row[16]) if row[16] else None
        three_att = float(row[17]) if row[17] else None
        fg_total = float(row[14]) if row[14] else None
        mp = float(row[12]) if row[12] else None

        if year and three_made is not None and three_att is not None and fg_total is not None and mp is not None:
            print(f"{year}\t{three_made},{three_att},{mp},1")
    except Exception as e:
        continue  # Skip malformed rows
