my_string = "123"
my_other_string = "one two three"

my_float = 4.0
my_other_float = 3.14

my_bool = True

my_truthy_int = 123
one = 1
my_falsey_int = 0

my_falsey_string = ""

print(int(my_float))
print(int(my_other_float))
print(int(my_string))

# does not work
# int(my_other_string)

print(float(my_string))

print(bool(my_falsey_int))
print(bool(one))
print(bool(my_truthy_int))

print(bool(my_string))
print(bool(""))

print(str(my_other_float))