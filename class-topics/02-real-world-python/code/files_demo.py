import os

PATH = os.path.join("data", "demo.txt")
print(PATH)

# with open(PATH, "r") as file:
# 	text = file.read()
# 	print(text)

with open(PATH, "r") as file:
	for line in file:
		print(line.strip())

# with open(PATH, "r") as file:

# 	lines = file.readlines()

# 	print(lines)

# 	for line in lines:
# 		print(line)

# with open(PATH, "r") as file:

# 	for line in file:
# 		print(line)

# 	result = file.readlines()
# 	print(result)

