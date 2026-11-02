"""Build data/normal.csv and data/attacks.csv from the Egger et al. files.

Run from the repository root. All attack classes become label 1.
"""
import csv
from pathlib import Path

RAW = Path("data/raw/energy-informatics-2020")
OUT = Path("final/data")
OUT.mkdir(exist_ok=True)

with open(OUT / "normal.csv", "w", newline="") as n, open(OUT / "attacks.csv", "w", newline="") as a:
    normal, attacks = csv.writer(n), csv.writer(a)
    for i, name in enumerate(["csvDataFeaturesTrain.csv", "csvDataFeaturesTest.csv"]):
        with open(RAW / name, newline="") as f:
            rows = csv.reader(f, delimiter=";")
            header = next(rows)
            if i == 0:
                normal.writerow(header)
                attacks.writerow(header)
            for row in rows:
                if row[-1] == "0":
                    normal.writerow(row)
                else:
                    attacks.writerow(row[:-1] + ["1"])
