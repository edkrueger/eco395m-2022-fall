# list 

l1 = [3, 5, 6, 8, 3, 2]
l2 = [2, 1, 3, 5, 6.0, 2]

# print(l1 + l2)

# print(l1 * 2)
# print(5 * l1)

# print(3.14 in l2)
# print(6 in l1)

# print(6.0 in l1)
# print(6.0 == 6)
# print(6 in l2)
# print(6 == 6.0)

# list method (in-place)

# l1.sort()
# print(l1)

# l2.reverse()
# print(l2)

# look mutation is wierd
# l1.reverse()
# print(l1)

# more mutation
# my_list = [1, 2, 6, 3, 7, 9]
# returned = my_list.sort()
# print(returned)
# print(my_list)

# how about copying -- wrong way
# original = [1, 2, 6, 3, 7, 9]
# bad_copy = original
# bad_copy.sort()
# print(bad_copy)
# print(original)

# how about copying -- a right way
# original = [1, 2, 6, 3, 7, 9]
# copy = original[:]
# copy.sort()
# print(copy)
# print(original)

# how about copying -- a right way
# original = [1, 2, 6, 3, 7, 9]
# copy = [*original]
# copy.sort()
# print(copy)
# print(original)

# lets avoid the problem all together
l = [23, 534, 756, 2, 654, 7]
l_sorted = sorted(l)
l_reversed = list(reversed(l))

print(l)
print(l_sorted)
print(l_reversed)

# string are immutable
s = "HellO world "
print(s.upper())
print(s)
print(s.upper().title())
print(s)

# tuples
t = (1, 2, 5, 3)
print(sorted(t))
print(t)
print(t + t)
print(t * 9)
print(2 * t)
print(t[1])
print(t[1:3])

# tuples of length 1
tl1 = (1,)
print(type(tl1))

# tuples of length 0
tl0 = ()
print(type(tl0))

# some common error

# AttributeError
# t.sort()

# IndexError
# print(tl1[1])

print(tl1[:100])