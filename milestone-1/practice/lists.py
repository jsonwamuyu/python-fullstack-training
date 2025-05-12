"""Python Lists"""

# Empty list
my_list = []


# Create a list
list_one = ["one", 1, "two", 2, [1, 2, 3]]

# Indexing a list
print(list_one[0])  # Prints the first item in a list -> 'one'.
print(list_one[-1])  # Print the last item -> [1,2,3].

# List slicing
print(list_one[1:4])  # prints item index 1 to index 3. Rem we exclude 4.

# Updating List -> replacing the value of item in that index.
list_one[1] = 'updated'
print(list_one)

# Appending/Adding an item
list_one.append('Appended')
list_one.append([5,6,7])

# Inserting at specific index
list_one.insert(4, 'Inserted')
print(list_one)