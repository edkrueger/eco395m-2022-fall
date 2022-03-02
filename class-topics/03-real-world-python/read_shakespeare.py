import os

path_ = os.path.join("data", "shakespeare", "shakespeare.txt")

print(path_)

with open(path_, "r") as in_file:
    for _ in range(20):
        print(in_file.readline())