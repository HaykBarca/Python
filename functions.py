# Required paramaters functions
def even_odd(num):
  if num % 2 == 0:
    return 'even'
  elif num % 2 != 0:
    return 'odd'

print(even_odd(2))
print(even_odd(3))

def param_fun(x, y, z):
  return x + y + z

print(param_fun(1, 2, 3))

# Optional parameters funtions
def f(x = 10):
  print(x)

f()
f(0)

# Required paramaters should be passed always before optional
def required_optional(x, y = 12):
  print(x + y)
required_optional(5)

# Nested functions
def outer():
  print("Outer!")
  def nested():
    print("Nested!")
  nested()
outer()