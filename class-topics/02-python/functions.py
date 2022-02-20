def say_hello():
	print("Hello World")

def return_hello():
	return "Hello World"

def double_sum(num_1, num_2):
	return 2 * (num_1 + num_2)

say_hello_result = say_hello()
print(say_hello_result)

return_hello_result = return_hello()
print(return_hello_result)

print(double_sum(3, 4))
print(double_sum("3", "4"))

# doesn't work
# print(double_sum(3, "4")) 
