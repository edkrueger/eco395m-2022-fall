with open("some_text.txt", "r") as in_file:
    
    # reading in a whole text file

    # print(in_file.read())

    # read line by line

    # for line in in_file:
    #     print(line.strip())

    # list_of_lines = in_file.readlines()
    # print(list_of_lines)

    # a little more control
    header = in_file.readline().strip()
    the_rest = in_file.read()

    print(header)
    print(the_rest)


