import os
import csv

PATH = os.path.join("data", "facebook", "reaction_counts.csv")

with open(PATH, "r") as in_file:

	csv_reader = csv.reader(in_file)

	header = next(csv_reader)

	print(header)

	data = []

	for row in csv_reader:
		print(row)
		break
		data.append(row)



	print(data)