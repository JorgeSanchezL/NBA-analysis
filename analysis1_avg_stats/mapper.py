#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header

for row in reader:
    # Check if the essential columns are available and valid
    try:
        year = row[1] if row[1] else None
        pts = float(row[34]) if row[34] else None
        ast = float(row[29]) if row[29] else None
        trb = float(row[28]) if row[28] else None

        # Only process rows where we have the necessary values (year, PTS, AST, TRB)
        if year and pts is not None and ast is not None and trb is not None:
            print(f"{year}\t{pts},{ast},{trb},1")
    except Exception as e:
        continue  # Skip malformed rows
