import os
import csv

PATH = os.path.join("data", "facebook", "reaction_counts.csv")
STATUS_TYPE_IDX = 3

with open(PATH, "r") as in_file:

    csv_reader = csv.reader(in_file)

    header = next(csv_reader)

    status_types = set()

    for row in csv_reader:
        status_types.add(row[STATUS_TYPE_IDX])

print(status_types)
