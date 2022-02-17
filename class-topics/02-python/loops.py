### print elements from list ###

l = ["Hello", "World", "GoodBye"]

for e in l:
	print(e)

for i in range(len(l)):
	print(i)
	print(l[i])

i = 0
while i < len(l):
	print(i)
	print(l[i])
	i = i + 1

### a closer look at range

r = range(10)
print(type(r))
print(list(r))

l = [1, 2, 5]
print(len(l))
print(range(len(l)))
print(list(range(0, 10)))
print(list(range(2, 10)))

### An infinite loop ###

# while True:
# 	print("Pizza")

###  print out even numbers ###

def print_evens_with_range(max_number):

	for number in range(0 ,max_number + 1, 2):
		print(number)
	return


def print_evens_with_mod(max_number):

	for number in range(0 ,max_number + 1):
		if number % 2 == 0:
			print(number)
	return


def print_evens_with_while(max_number):

	num = 0

	while num <= max_number:
		print(num)
		num = num + 2

	return

print_evens_with_range(20)
print_evens_with_mod(20)
print_evens_with_while(20)

### summing up a list ###

def sum_by_element(l):

	sum_ = 0

	for e in l:
		sum_ = sum_ + e

	return sum_

def sum_by_index(l):

	sum_ = 0

	for i in range(len(l)):
		sum_ = sum_ + l[i]

	return sum_

def sum_with_while(l):

	sum_ = 0

	i = 0 
	while i < len(l):
		sum_ = sum_ + l[i]
		i = i +1

	return sum_

my_list = [2, 5, 7, 3, 5, 34]
print(sum(my_list))
print(sum_by_element(my_list))
print(sum_by_index(my_list))
print(sum_with_while(my_list))




