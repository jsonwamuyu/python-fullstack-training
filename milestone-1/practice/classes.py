"""
Class variables are defined at class level while instance variables
are defined inside methods using self.

When class variable is changed, it affects all the instances unless overridden by instance variable
self refers to the current instance of the class

"""

class Employee:

    # Class variable - store data that want to be shared across all instances (objects).
    company_name = 'Twitter Inc.'

    def __init__(self, fullname, title, salary):
        # Instance variable - store data that is unique to each object (instance of a class).
        self.fullname = fullname
        self.title = title
        self.salary = salary


emp1 = Employee('John Doe', 'Manager', 45000)
print(emp1.fullname)

emp2 = Employee('Jane Doe', 'Secretary', 20000)
print(emp2.fullname)

print(emp1.company_name) # Twitter Inc.
print(emp2.company_name) # Twitter Inc.
print(Employee.company_name) # Twitter Inc.
