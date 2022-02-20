# string methods
# https://docs.python.org/3.7/library/stdtypes.html#string-methods

my_str = "heLlO"
cap_str = my_str.capitalize()
print(my_str)
print(cap_str)

print(my_str.lower())
print(my_str.swapcase())

print(my_str.capitalize().swapcase())
print(my_str.swapcase().capitalize())

# lists indexing

my_list = ["a", "b", "c"]
my_mixed_list = [1, 3.14, 8j, "asdas", [1, 2, 3]]

print(my_list[0])
print(my_list[1])
# next line causes an IndexError
# print(my_list[3])
print(my_list[-1])

# list slicing

my_longer_list = [2, 4, 6, 8, 10]
print(my_longer_list[1:3])
my_ints = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_ints[::2])
print(my_ints[::-1])

# strings indexing and slicing

print(my_str[3])
print(my_str[1:3])


