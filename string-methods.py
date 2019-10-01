# String Manipulation
# Triple String are string that grabe more than one line
my_string = """Hello
My
Dear
Friend
"""
print(my_string)

# String are iterable
it_string = "Hayk loves barca"
print(it_string[2]) # Also strings are immutable, you cant change haracters of the string
print(it_string.upper()) # Objects have some built-in methods, upper() makes string characters uppercase, the opposite lower()
print(it_string.capitalize()) # Capital every first letter of sentence

# Format methods
year_started = "1989"
creator = "Guido van Rossum"
print("Python was created in {}. And its created by {}".format(year_started, creator))

# Split() splits string into separate lists
stringish = "Hey, split it here.And return me new list"
print(stringish.split("."))
new_list = stringish.split(".")
print(". ".join(new_list)) # jon() Joins List items into one string
print(stringish.replace("e", "A")) # replace() Replace given characters
print(stringish.index("e")) # index() Returns given character's first index
print("Hayk " + "loves " + "Barca!") # Concatenation
print("cat"*3) # Multiples string given times
