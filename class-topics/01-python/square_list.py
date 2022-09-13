my_list = [12, 4, 6, 8, 9]

def square(list_):

	out_list = []

	for e in list_:
		out_list.append(e ** 2)

	return out_list

def square_comprehension(list_):

	return [e ** 2 for e in list_]

def square_map(list_):
	return list(map(lambda x: x ** 2, list_))

print(square(my_list))
print(square_comprehension(my_list))
print(square_map(my_list))


def vect_add(list_a, list_b):

	out_list = []

	for e_a, e_b in zip(list_a, list_b):
		out_list.append(e_a + e_b)

	return out_list

def vect_add_comprehension(list_a, list_b):
	return [e_a + e_b for e_a, e_b in zip(list_a, list_b)]

vect_a = [1, 2, 3]
vect_b = [5, 7, 9]

print(vect_add(vect_a, vect_b))
print(vect_add_comprehension(vect_a, vect_b))

