def get_next_collatz_term(n):
	"""Find the next term given a term."""

	if n % 2 == 0:
		return n // 2
	else:
		return 3 * n + 1


def collatz(n):
	"""Returns the sequence as a list."""

	sequence = []

	while True:
		sequence.append(n)

		if n == 1:
			break

		n = get_next_collatz_term(n)

	return sequence

print(collatz(10))
print(collatz(145))




