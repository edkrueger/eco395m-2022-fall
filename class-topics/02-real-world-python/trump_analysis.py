import os
import csv

IN_PATH = os.path.join("data", "facebook", "reaction_counts.csv")
OUT_PATH = os.path.join("data", "facebook", "reaction_counts_agg.csv")

STATUS_TYPE_IDX = 3
NUM_SHARES_IDX = 8

def agg_by_num_shares(path):

	# this is to keep track of the status types that we've encountered
	status_types = set()

	counts = {}
	totals = {}

	with open(path, "r") as in_file:

		csv_reader = csv.reader(in_file)

		next(csv_reader)

		for row in csv_reader:
			
			status_type = row[STATUS_TYPE_IDX]
			num_shares = int(row[NUM_SHARES_IDX])

			if status_type in status_types:

				counts[status_type] += 1
				totals[status_type] += num_shares

			else:

				status_types |= {status_type}

				counts[status_type] = 1
				totals[status_type] = num_shares

	return status_types, counts, totals


status_types, counts, totals = agg_by_num_shares(IN_PATH)


fieldnames = status_types | {"agg"}

with open(OUT_PATH, "w+") as out_file:

	csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
	csv_writer.writeheader()
	csv_writer.writerow({**counts, "agg": "count"})
	csv_writer.writerow({**totals, "agg": "total"})









print(status_types)
print(counts)
print(totals)