""""
Dictionary

A key-value pair collection, keys are unique i.e. must be immutables (string, tuples, numbers)
Values can be any type
"""

# Create dictionary
car = {'make':'Toyota', 'year':2002}

# Access
print(car['make'], car['year'])
print(car.get('model')) # None (safe)

# Add/Update
car['model'] = 'Benz'
car['color']= 'blue'

car['color'] ='red' # Update color from blue to red


# Delete
car['manufacturer'] = 'Wazee'
del car['manufacturer']
car.pop('model')

print(car)


# Useful Methods
d = {'a':1, 'b':2, 'c':3}
print('Keys:', d.keys())
print('Values', d.values())
print('Items', d.items())

for key, value in d.items():
    print(f'{key} -> {value}')

"""
Problem:

Given a list of integers, return a dictionary where 
the key is the number and the value is the count of its occurrences.
"""
print("==============================================\n")
def count_freq(nums):
    freq = {}
    print('Empty freq',freq)
    for num in nums:
        # Check whether num already in freq
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1 # Assigning key = num and value 1
    return freq

print(count_freq([1,6,3,6,1])) # {1:2, 6:2, 3:1}
print(count_freq([7,3,9,4,4,3,2,6,7]))