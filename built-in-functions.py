# Built-in functions in Python

# Length of an object
length = len("Mammal")
print(length)

# Type of an object
print(type(100))
print(type('Hayk'))
print(type(2.3))

# Data convertation
print(str(101))
print(str(False))
print(int('101'))
print(float('101'))

# Input
def get_info():
  age = input("How old are you\n")
  age = int(age)
  if age < 18:
    print("You're not allowed to enter, your age is", age)
  else:
    print("Welcome", age)
get_info()