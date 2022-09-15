print("Hello")

print(45 * "8")

my_str = "HeLLO WorLd"

print(my_str.upper())
print(my_str.title())
print(my_str.lower())
print(my_str.swapcase())

print(my_str.title().swapcase())

my_silly_list = [1, 2, "4", 4 + 6j, [1, 2, 3], 3.5]
print(my_silly_list)

my_list = [1, 4, 6, 3, 7, 9]
print(my_list)

print(my_list[0])
print(my_list[4])

# Expected to give an IndexError
# print(my_list[1000])

print(my_list[-1])
print(my_list[-2])

print(my_list[3:5])
print(my_list[:5])
print(my_list[3:])

print(list(range(0, 10)))
print(list(range(10)))
print(list(range(0, 100, 2)))

first_hundred = list(range(100))

print(first_hundred[0:50:2])

print(first_hundred[::-1])

first_hundred_list_str = [str(e) for e in first_hundred]
print(first_hundred_list_str)

print(", ".join(first_hundred_list_str))

first_hundred_str = "".join(first_hundred_list_str)

print(first_hundred_str)

print(first_hundred_str[0])
print(first_hundred_str[0:10])
print(first_hundred_str[::2])

l1 = ["a", "b", "c", "d"]
l2 = ["e", "f", "g"]
l3 = [1, 2, 3, 4, 5]
l4 = [13, 26, 32, 14, 5]

print(l1 + l2)
print(l3 + l4)
print(3 * l3)

print("b" in l1)
print("z" in l1)

print(l1 == l1)
print(l1 == l3)

# not mutating

x = "asdf"
print(x)
x = x + x
print(x)

# mutation
l4 = [1,2,3,5]
print(l4)
l4[-1] = 4
print(l4)

print(l4.sort())
print(l4)

# mutation is evil!
l5 = [1, 3, 2, 4, 5]
l6 = l5
l6.sort()
print(l6)
print(l5)

# deal with it
l5 = [1, 3, 2, 4, 5]
l6 = l5[:]
l6.sort()
print(l6)
print(l5)

# used sorted
l5 = [1, 3, 2, 4, 5]
l6 = sorted(l5)

# tuples
t5 = (1, 3, 2, 4, 5)
print(t5[3])
print(t5[3:])
print(sorted(t5))

# mutation -- won't work
t4 = (1,2,3,5)
print(t4)

# expected TypeError
t4[-1] = 4









