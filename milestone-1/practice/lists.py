"""Python Lists"""

# Empty list
my_list = []


# Create a list
list_one = ["one", 1, "two", 2, [1, 2, 3]]
S = list_one[1]

# Indexing a list
print(list_one[0])  # Prints the first item in a list -> 'one'.
print(list_one[-1])  # Print the last item -> [1,2,3].

# List slicing
print(list_one[1:4])  # prints item index 1 to index 3. Rem we exclude 4.

# Updating List -> replacing the value of item in that index.
list_one[1] = "updated"
print(list_one)

# Appending/Adding an item
list_one.append("Appended")
list_one.append([5, 6, 7])

# Inserting at specific index
list_one.insert(4, "Inserted")
print(list_one)

# Removing an item in the list
list_one.remove("one")  # Remove the first occurrence
print("one has been removed", list_one)

# Deleting by index
del list_one[2]
print("Deleting at index 2: ", list_one)

# Remove the last and return it
popped = list_one.pop()
print("Popped the last item:", popped)

# Filtering a list
new_list = [1, 5, 9, 0, 4, 0, 3, 0]
non_zero_list = [new for new in new_list if new != 0]
print("Filtered list:", non_zero_list)  # Removed all zeros in the list
# Rem you can not use remove() in a loop - inefficient/can cause error

usernames = ["john", "", None, "jane"]
cleaned = [name for name in usernames if name]
print("Remove empty and none values:", cleaned)

# Remove duplicates
duplicate = ["one", "one", 1, 1, 4, 5, 4, 5]
remove_duplicates = set(duplicate)
print("Removed duplicates:", remove_duplicates)

# Searching item in a list
print("Searching - return true if present.", "one" in duplicate)
print("two" in duplicate)
print("Search using index", duplicate.index("one"))

# List length
print("Length of the list", len(duplicate))

"""
Problem: Given a list of numbers,
write a function to remove all even numbers in-place and return the resulting list.
"""

def remove_even_numbers(even_nums):
    # Make a shallow copy.
    for num in even_nums[:]:
        if num % 2 == 0:
            even_nums.remove(num)
    return even_nums


print('No even numbers', remove_even_numbers([]))
print('No even numbers', remove_even_numbers([23,4,5,6,7,8,9,0,10]))
