def is_even(x):
	
	return x % 2 == 0

print(is_even(4323423))
print(is_even(4323422))


def truthy_fun(str_):

	if str_:
		print("This is fun")
	else:
		print("This is not fun")


truthy_fun("hello")
truthy_fun("")
truthy_fun(123)
truthy_fun(0)

def grade_print(grade_num):

	if grade_num >= 90:
		print("A")
	elif grade_num >= 80:
		print("B")
	elif grade_num >= 70:
		print("C")
	elif grade_num >= 60:
		print("D")
	else:
		print("F")

grade_print(90)
grade_print(30)
grade_print(66)

def grade(grade_num):

	if grade_num >= 90:
		return "A"
	if 80 <= grade_num < 90:
		return "B"
	if 70 <= grade_num < 80:
		return "C"
	if 60 <= grade_num < 70:
		return "D"
	
	return "F"

def grade_print_two(grade_num):
	print(grade(grade_num))

grade_print_two(90)
grade_print_two(30)
grade_print_two(66)



