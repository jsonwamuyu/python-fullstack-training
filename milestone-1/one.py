import os
import sys


def say_hello(name="World"):
    print("Hello," + name)


class PersonTwo:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def greet(self):
        print(f"Hello, {self.full_name}. You are {self.age} years old.")
        print("Hello, " + self.full_name + ". You are ", str(self.age), "years old.")


# Call function.
say_hello()


p = PersonTwo("Alice King", 23)
p.greet()


class Car:
    def __init__(self, brand, year):
        self.year = year
        self.brand = brand

    def drive(self):
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
#           Adds a function is_minor() that checks if the person is under 18, returning True or False.
#                   If the user is a minor, print: "You are a minor."
#                   Otherwise, print: "You are an adult."


class Person:
    """Represents a person with name and age."""

    def __init__(self, name, age):
        """Initializes the name and age of person."""
        self.name = name
        self.age = age

    def greet(self):
        """Greets the user with name and age."""
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


emoji = "😊"
print(emoji)
print(type(emoji))


def hello():
    """The doc string should not exceed 79 characters."""
    name = input("Enter your name: ")
    print(f"Hello {name}")


hello()


def connect_database(greetings=None):
    print("Connected to database")
    return greetings
