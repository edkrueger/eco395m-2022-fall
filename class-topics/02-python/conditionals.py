def say_even_or_odd(my_int):
	if my_int % 2 == 0:
		print("It is even!")
	else:
		print("It is odd!")

def great_good_or_bad(my_int):
	if my_int % 2 == 0:
		print("Great")
	elif my_int % 3 == 0:
		print("Good")
	else:
		print("Bad")

def fizzbuzz(my_int):
	
	if (my_int % 3 == 0) and (my_int % 5 ==0):
		print("fizzbuzz")
	elif my_int % 3 == 0:
		print("fizz")
	elif my_int % 5 == 0:
		print("buzz")

# say_even_or_odd(2)
# say_even_or_odd(55)

# great_good_or_bad(3)
# great_good_or_bad(2)
# great_good_or_bad(6)
# great_good_or_bad(5)

fizzbuzz(6)
fizzbuzz(10)
fizzbuzz(15)
fizzbuzz(2)