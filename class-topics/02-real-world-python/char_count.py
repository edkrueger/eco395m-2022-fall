import pprint

def char_count(str_):

	char_counts = {}

	for char_ in str_:

		if char_ in char_counts:
			char_counts[char_] += 1
		else:
			char_counts[char_] = 1

	return char_counts

str_1 = "wlqdwmtcyliuartmylrsytcluimryliuwemahtcilus"

result = char_count(str_1)
print(result)
pprint.pprint(result)

pprint.pprint(list(result.items()))

pprint.pprint(
	sorted(result.items(), key=lambda e: e[1], reverse=True)
	)