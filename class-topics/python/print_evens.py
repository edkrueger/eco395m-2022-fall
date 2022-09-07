def print_evens_w_range(n):
	for e in range(0, n, 2):
		print(e)

print_evens_w_range(5)


def print_evens_w_mod(n):
	for e in range(n):
		if e % 2 == 0:
			print(e)

print_evens_w_mod(5)

def print_evens_w_while(n):

	i = 0

	while i < n:
		if i % 2 == 0:
			print(i)
		i += 1
		
print_evens_w_while(5)

 


