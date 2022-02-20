a = "my string"
b = 'my string 2'
c = """
my long 
string
"""

print(a)
print(b)
print(c)

print(a + b)

print(5 * a)
print(a * 5)

print(50 * "=")

answer = int(input("What is your favorite number? "))
five_answer = 5 * answer

print("Five times your favorite number is " + str(five_answer) + ".")
print(f"Five times your favorite number is {five_answer}.")