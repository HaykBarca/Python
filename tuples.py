# A tuple is an immutable container that stores objects in a specific order
my_tuple = tuple()
print(my_tuple)

my_new_tuple = ()
print(my_new_tuple)

# You should add items when you creating tuple, you can't change, add, remove items from tuple
tuple_items = ("Apple", "Orange")
print(tuple_items)
print(tuple_items[1])
new_tuple_items = tuple_items[0:1] # Slice tuple
print(new_tuple_items)
print("Orange" in tuple_items) # Check if Orange exists in tuple