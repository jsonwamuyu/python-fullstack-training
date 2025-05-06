"""For loops (counting through items) and While loops (based on conditions)"""

# For loop is used to iterate over sequences(dic,string, lists, tuples, sets)

# Syntax

#  for variable in sequence:
#       code block

fruits = ["Oranges", "Mango", "Apple", "Kiwi", 'Pipini']
students = {'johnson':34, "mike":32, "History":35}

for fruit in fruits:
    print(fruit)

for key in students.keys():
    print(key)

for value in students.values():
    print(value)

for key, value in students.items():
    print(key, value)


for key in students:
    print('Student key',key, students[key])

for num in range(10):
    print("*" * num)


my_numbers = [23, 56, 45, 67, 44]


age = int(input('Enter your age: '))
if age < 18:
    print('Minor')
elif age == 18:
    print('You have turned 18')
else:
    print("You can have a driver license.")
