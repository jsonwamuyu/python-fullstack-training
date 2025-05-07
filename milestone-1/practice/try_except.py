"""
Exception handling with try, except, else, and finally

Try: This block will test the excepted error to occur
Except:  Here you can handle the error
Else: If there is no exception then this block will be executed
Finally: Finally block always gets executed either exception is generated or not
"""

NUM_ONE = 10
NUM_TWO = 0

try:
    results = NUM_ONE / NUM_TWO
    print("Results: ", results)

except ZeroDivisionError:
    print("Sorry, no division by zero allowed.")
