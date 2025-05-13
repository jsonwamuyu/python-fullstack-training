"""
SETS

An ordered collection of unique elements.
It is mutable but its elements MUST be immutable
"""

# Creating sets
set_one = {1, 3, 4}
set_empty = set()  # {} creates an empty dict

# Adding elements
set_empty.add(2)
print(set_empty)


# Removing elements
set_empty.remove(2)  # Raises an error if not found.
set_empty.add(3)
set_empty.discard(2)  # No error if 2 not found.
print(set_empty)

# Membership test
set_empty.add(2)
set_empty.add(2)
print(2 in set_empty)  # Print True


# Set length - number of unique element
print(set_empty)
print(len(set_empty))


# Set Operations
set_num1 = {1, 2, 3, 4}
set_num2 = {3, 4, 5, 6}
print("a union b:", set_num1.union(set_num2))  # Combine both sets {1,2,3,4,5,6}
print(
    "a intersection b", set_num1.intersection(set_num2)
)  # What common in both sets 3, 4
print("a difference b", set_num1.difference(set_num2))  # Elements in a not in b {1, 2}
print("b difference a", set_num1.difference(set_num2))  # Elements in b not in a  {5, 6}

print(
    "a symmetric_difference(b)", set_num1.symmetric_difference(set_num2)
)  # Remove shared items and combine the rest i.e. elements in a or b but not in both


"""
Problem:

Write a function has_duplicates(nums) that returns True 
if there are any duplicates in the list, otherwise False.
"""

def has_duplicates(nums):
    duplicates = set()
    for num in nums:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False

print(has_duplicates([1, 2, 3, 4]))     # ➞ False
print(has_duplicates([1, 2, 3, 2]))     # ➞ True
print(has_duplicates([]))           # ➞ False
print(has_duplicates([5, 5, 5, 5]))     # ➞ True