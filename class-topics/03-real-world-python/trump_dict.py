import os
import csv

PATH = os.path.join("data", "facebook", "reaction_counts.csv")

with open(PATH, "r") as in_file:

    dict_reader = csv.DictReader(in_file)
 
    status_count = {}

    for row in dict_reader:

        num_shares = int(row["num_shares"])
        status_type = row["status_type"]

        if status_type in status_count:
            status_count[status_type] += num_shares
        else:
            status_count[status_type] = num_shares

print(status_count)
