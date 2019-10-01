new_file = open("hello.txt", "w") # 'w' stands for 'write', 'w+' read and write, 'r' stands for reading
new_file.write("Here I can meet you")
new_file.close()

# Preferable syntax is here
with open("hello2.txt", "w") as my_file:
  my_file.write("Another method.")