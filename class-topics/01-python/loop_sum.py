my_list = [3, 4, 5, 6, 3]

print(sum(my_list))

def sum_with_for_elem(list_):

	sum_ = 0

	for e in list_:
		sum_ += e

	return sum_

print(sum_with_for_elem(my_list))


def sum_with_for_idx(list_):

	sum_ = 0

	for i in range(len(list_)):
		sum_ += list_[i]

	return sum_

print(sum_with_for_idx(my_list))
