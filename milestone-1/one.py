"""Learning and practicing python."""

# import os
# import sys

# OPERATORS

NUM_ONE = 5
NUM_TWO = 2
# Arithmetics operators - performs mathematical computations
print("Addition: ", NUM_ONE + NUM_TWO)
print("Subtraction: ", NUM_ONE - NUM_TWO)
print("Division:", NUM_ONE / NUM_TWO)
print("Floor division: ", NUM_ONE // NUM_TWO)
print("Multiplication:", NUM_ONE * NUM_TWO)
print("Modulus: ", NUM_ONE % NUM_TWO)
print("Exponential: ", NUM_ONE**NUM_TWO)


# The double division operator (//) in Python 3 returns the floor
# value for both integer and floating-point arguments after division.

print("Double division operator: ", 7 // 3)
print("Single division operator: ", 7 / 3)


# Comparison or Relational Operator.
# compare values and returns a boolean value (True or False)
# according to the condition.

print("Greater than: ", NUM_ONE > NUM_TWO)
print("Less than: ", NUM_ONE < NUM_TWO)
print("Equal to: ", NUM_ONE == NUM_TWO)
print("Not equal to: ", NUM_ONE != NUM_TWO)
print("Greater or equal to: ", NUM_ONE >= NUM_TWO)
print("Less or equal to: ", NUM_ONE <= NUM_TWO)


# Logical operators
# Combine conditional statements - By performing LOGICAL AND, OR, NOT.
IS_TRUE = True
IS_FALSE = False
print("Logical AND:", IS_TRUE and IS_FALSE)
print("Logical OR: ", IS_TRUE or IS_FALSE)
print("Logical NOT: (Negate)", not IS_FALSE)  # Negating the value.
print("Logical NOT: ", not IS_TRUE)  # False


# Bitwise operators
# Act on bits and perform bit-by-bit operations.
# These are used to operate on binary numbers.

# TODO


# Assignment operator
# Assign values to variables - assign the value of the right side
# of the expression to the left side operand

a=10
print('a should be 10', a)
b=a
print('b is now assigned to value of a which is 10 ', b)
print('a id is: ', id(a))
print('b id is: ', id(b))

print('Is a and b id the same: ',id(a) == id(a))

a = 45
print('Now a is reassigned to 45', a)
print(f'b is {b} after reassigning a')

print('does a still have the same id as b', id(a) == id(b))

# "is" for identity operator(checks whether they point to the same object)
# while "==" is for equality operator(compare the object content)

my_list = [1,2,3,4]
my_list_two = my_list
# They both point to the same object

my_list.append(5)
# Now you are changing the object content(mutating)
# which will also update my_list_two

my_list = [1,3,4]
# This now will reassign myList to point to a new object
# and the original object remains intact

# Special operators

def say_hello(name="World"):
    """Print a hello message with name"""

    print("Hello," + name)


class PersonTwo:
    """Create Person object with name and age."""

    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def person_details(self):
        """Print person details"""

        print(f"Fullname: {self.full_name}, Age: {self.age}")

    def greet(self):
        """Greet person with fullname and age."""

        print(f"Hello, {self.full_name}. You are {self.age} years old.")
        print("Hello, " + self.full_name + ". You are ", str(self.age), "years old.")


# Call function.
say_hello()


p = PersonTwo("Alice King", 23)
p.greet()


class Car:
    """Define Car object with brand and year."""

    def __init__(self, brand, year):
        self.year = year
        self.brand = brand

    def __str__(self):
        pass

    def drive(self):
        """Print brand driving."""
        print(f"{self.brand} is driving")


benz = Car("Benz", 1990)
benz.drive()

my_car = Car("Toyota", 2001)
my_car.drive()

# Write a Python program that:
#     1. Asks the user for their name and age.
#     2. Prints a message showing:
#
#         Their name.
#
#         Their age in months.
#
# 💡 Bonus: If the user is under 18, print "You are a minor." Otherwise, "You are an adult."


def print_user_name_age():
    """Prompt user for name and age - print them."""

    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    print(f"Your name is {name} and age is {age*12} months.")
    if age < 18:
        print("You are minor")
    else:
        print("You are an adult")


print_user_name_age()

# ✅ Task:
# Write a Python program that:
#   Defines a Person class with:
#       Attributes: name, age
#       Method: greet() that prints: "Hi, my name is <name> and I am <age> years old."
#       Asks the user to input their name and age.
#           Instantiates a Person object and calls the greet() method.
#           Adds a function is_minor() that checks if the person is
#           under 18, returning True or False.
#                   If the user is a minor, print: "You are a minor."
#                   Otherwise, print: "You are an adult."


class Person:
    """Represents a person with name and age."""

    def __init__(self, name, age):
        """Initializes the name and age of person."""
        self.name = name
        self.age = age

    def __str__(self):
        pass

    def greet(self):
        """Greets the user with name and age."""
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


EMOJI = "😊"
print(EMOJI)
print(type(EMOJI))


def hello():
    """The doc string should not exceed 79 characters."""
    name = input("Enter your name: ")
    print(f"Hello {name}")


hello()


def connect_database(greetings=None):
    """Establish database connection."""
    print("Connected to database")
    return greetings
