import csv

with open("my_dict_csv.csv", "w+") as out_file:

    header = ["hello", "world"]

    dict_writer = csv.DictWriter(out_file, fieldnames=header)
    dict_writer.writeheader()

    data = [
        {"hello": 1, "world": 2},
        {"hello": 3, "world": 4},
        {"hello": 5, "world": 6},
    ]

    dict_writer.writerows(data)