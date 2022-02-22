import csv

with open("my_csv.csv", "w+") as out_file:
    csv_writer = csv.writer(out_file)

    header = ["hello", "world"]

    data = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    csv_writer.writerow(header)
    csv_writer.writerows(data)