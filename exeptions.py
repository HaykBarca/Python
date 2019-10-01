# Exeption handling
num1 = input("Please input a number\n")
num2 = input("Please inout second number\n")

try:
  print(int(num1)/int(num2))
except ZeroDivisionError:
  print("One of the arguments are zero")

# Docstrings (some type of comments)
def pyramid(height = 8):
  """
    height parameter defines the height of the pyramid blocks
  """
  for i in range(height + 1):
    line = ""
    for j in range(i):
      line += "#"
    print(line)

height = int(input("Enter the height.\n"))
pyramid(height)