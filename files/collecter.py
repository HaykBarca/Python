name = input('Your name?\n')
age = input('And your age?\n')

with open('collecter.txt', 'w') as my_file:
  my_file.write("Name: {}\nAge: {}".format(name, age))