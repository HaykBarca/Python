# For loops
for i in range(0, 5):
  print(i)

# Iterable strings
for i in "Python":
  print(i)

# While loops
x = 10
while x > 0:
  print("{}".format(x))
  x -= 1
print("Happy New Year!")

for i in range(0, 100):
  print(i)
  break # break keyword stops the loop

# Example of break
questions = ["What is your name?", "Favourite color?", "Quest?"]
n = 0
while True:
  print("Type 'q' to quit")
  answer = input(questions[n] + '\n')
  if answer == 'q':
    break
  n += 1
  if n > 2:
    n = 0

# Example of continue
for i in range(0, 5):
  if i == 3:
    continue
  print(i)