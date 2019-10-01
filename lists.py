# Lists (mutable container that stores objects)
my_list = list ("Apple")
print(my_list)

new_list = ["Apple", "Orange", "Peach"]
new_list.append("Banana")
new_list.append(100) # Append new item, can be any type
print(new_list)
print(new_list[2])
new_list[2] = "New Peach" # Mutate existing value
print(new_list[2])
new_list.pop() # Remove last item
print(new_list)

# Keyword 'not' checks if item not exists in list
color_list = ["Blue", "Red"]
print("Green" not in color_list)
print(len(color_list)) # len() can return the size of the list

# Slice returns a new list constructed by given indexes of the old list
slice_exmp = ["JS", "C", "Python", "Java"]
new_slice = slice_exmp[0:3]
print(new_slice)