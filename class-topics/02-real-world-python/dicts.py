from pprint import pprint

d = {}

d2 = {
	"hello": "a greeting",
	"world": "a place where things are",
	3: 1234
}

print(d)
print(d2)

print(d2["hello"])
print(d2["world"])
# expected to error
# print(d2[0])
print(d2[3])

result = d2.get("hello")
print(result)
result1 = d2.get(4)
print(result1)
result2 = d2.get(4, False)
print(result2)

real_dict = {
	"cat": ["A furry roomate"]
}

real_dict["dog"] = [
	"mans best friend",
	"a carnivorius mammal"
]

real_dict["dog"] = [
	"mans best friend",
	"a carnivorius mammal",
	"a furry pet"
]

real_dict["cat"].append("a carnivorius mammal")

print(real_dict)

print(real_dict.keys())
print("cat" in real_dict)
print("cat" in real_dict.keys())

print(real_dict.values())

print(real_dict.items())

for k in d2:
	print(f"Key: {k}")
	print(f"Value: {d2[k]}")

for e in d2.items():
	print(e)
	print(f"Key: {e[0]}")
	print(f"Value: {e[1]}")

for k, v in d2.items():
	print(e)
	print(f"Key: {k}")
	print(f"Value: {v}")

print({**d2, **real_dict, "asd": 123})

pprint({**d2, **real_dict, "asd": 123})








