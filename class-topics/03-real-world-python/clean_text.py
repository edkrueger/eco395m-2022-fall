# remove header and all caps

with open("some_text.txt", "r") as in_file:

    with open("out_file.txt", "w+") as out_file:

        header = in_file.readline()

        for line in in_file:
            out_file.write(line.upper())