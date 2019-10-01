# Dictionaries - mutable containers which maping one object to another (key: value)
my_dict = dict()
print(my_dict)

my_dict_lit = {}
print(my_dict_lit)

# Key: value pairs
fruits = {
  "Apple": "Red",
  "Banana": "Yellow"
}
print(fruits)
print(fruits["Banana"]) # Access to value

# Dictionaries are mutable
words = dict()

words["name"] = "Hayk"
words["surname"] = "Ghonakhchyan"
print(words)
print("name" in words) # Checks if key exists in dictionary
del words["surname"] # Delete the keyword from dict
print(words)