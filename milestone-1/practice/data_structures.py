"""
List, Tuple, Set, Dictionary, String
"""

print("This is awesome")

my_list = ["one", "two", "three", "four", 456, ["Jane", "Mike", 78]]

print(my_list[0])  # Print first item -> one
print(my_list[-1])  # Print the last item

print(my_list)  # Print the whole list
print(my_list[1:3])  # Slice from index 1 to 3

# append an element at the end
my_list.append("Appended")
print("New list after appending: ", my_list)

# Insert an element at a specif index
my_list.insert(2, "inserted")
print("New list after insertion: ", my_list)

# Extend the list
my_list.extend(["extended", "list"])
print("New list after extending: ", my_list)


list_two = []

print("Empty list: ", list_two)

list_two.append("First")

list_two.insert(1, "Second")

list_two.extend(["Third"])
list_two.extend("Third")

print("New list: ", list_two)


# Remove item - first occurrence
list_two.remove("Third")

print("List two after removing: ", list_two)

# Pop an element pop(index) -> removes and return element at index(default last)
list_two.pop()

print("List two after default pop: ", list_two)

list_two.pop(3)

print("List two after popping index 3: ", list_two)


# Clear the list
list_two.clear()
print("List two after clearing: ", list_two)


# Return index of first occurrence of an element.
print("Index of one: ", my_list.index("one"))
print("Index of two: ", my_list.index("two"))


# count() - return the occurrences of an element in a list
my_list.append("one")
print("Count of occurrence of one:", my_list.count("one"))


# sort() - sort list in place
list_numbers = [1, 4, 6, 7, 0, 6]
print("List numbers before sorting: ", my_list)
list_numbers.sort()
print("My list after sorting: ", list_numbers)


# sorted() - return the sorted list
my_nums = [3, 5, 2, 8, 5, 2, 8, 9, 4]
sorted_list = sorted(my_nums, reverse=True)
print("Sorted list:", sorted_list)
print("Occurrence of 2: ", my_nums.count(2))


# reverse() -


# len() - return the number of items in the list
print("Length of the list: ", len(my_nums))
print("All numbers: ", my_nums)
print("Print the last item in the list: ", my_nums[len(my_nums) - 1])


print('\n===================   Dictionaries   =========================')
# dictionary
my_dic = {}
print('Empty dic: ', my_dic)

# Adding an item
my_dic['username'] = 'John Doe'
print('My dic after adding an item: ', my_dic)


# Accessing item value
print('Get an item value using [key]', my_dic['username'])
print('Getting item value using get() method: ', my_dic.get('username'))



# 1. Create a dictionary of student info
student = {
    "name": "John",
    "age": 22,
    "courses": ["Math", "Physics"]
}
print("Initial dictionary:", student)

# 2. Add a new key "grade"
student["grade"] = "A"
print("After adding grade:", student)

# 3. Modify age
student["age"] = 23
print("After modifying age:", student)

# 4. Access courses
print("Courses:", student.get("courses"))

# 5. Remove grade
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)
print("After removing grade:", student)

# 6. Iterate over keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# 7. Use dictionary comprehension to create a dict of course name lengths
course_lengths = {course: len(course) for course in student["courses"]}
print("Course lengths:", course_lengths)

# 8. Clear the dictionary
student.clear()
print("After clearing:", student)
