s1 = {"a", "s"}
s2 = {"a", "s", "s"}
s3 = {"s", "d", "f", "g", "h"}
s4 = set("sdfg")

print(s1)
print(s2)
print(s1 == s2)
print(s3)
print(s4)

# not the empty set
d_mut = {}
print(type(d_mut))
print(d_mut)

# empty dict is Falsey
if d_mut:
	print("Thruthy")

# this is actually an empty set
s_mut = set()
print(type(s_mut))

# empty set is Falsey
if s_mut:
	print("Thruthy")

s_mut.add(1)
print(s_mut)

s_mut.add("1")
print(s_mut)

# with built-in types hashable coninsides with immutable
# expected to error
# s_mut.add({"1"})

# problem of mutability revisited
s_mut_2 = s_mut
s_mut_2.add(3)
print(s_mut_2)
print(s_mut)

# frozensets are immutable sets
fs = frozenset({1, 2, 3})
print(fs)
# expected to error
# fs.add(4)

# frozensets can go in (frozen)sets,
# becasue they are immutable (and hashable)
fs2 = frozenset({1, fs})
print(fs2)

s = {1, 2, 3}
s_v2 = s.union({4})
s_v3 = s | {4}
print(s_v2)
print(s_v3)

print(s2 & s3)
print(s2.intersection(s3))

print(s2 - s3)
print(s2.difference(s3))

print(s2 ^ s3)
print(s2.symmetric_difference(s3))

print("s" in s3)

print(s)













