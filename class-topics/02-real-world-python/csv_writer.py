import os
import csv

OUT_PATH = os.path.join("data", "out.csv")


data = [
		[1, 2],
		[3, 4]
	]

with open(OUT_PATH, "w+") as out_file:

	csv_writer = csv.writer(out_file)

	csv_writer.writerow(["a", "b"])
	for row in data:
		csv_writer.writerow(row)