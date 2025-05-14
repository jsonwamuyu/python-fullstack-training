"""
String

Sequence of character enclosed with double/single quotes.
Strings are ordered - have a fixed order
You can slice or index them
You can not change characters in strings once you crate them - instead you create a new string
Strings are iterable - can loop through them like list
They have length
"""

firstname = "Johnson"
print(firstname.lower())  # Convert to lowercase
print(firstname.upper())  # Convert to uppercase

print("Return index", firstname.find("s"))  # return the index of first match.
print("Replace some text", firstname.replace("son", "daughter"))

print("Sprint", "a,b,c,d".split(","))  # Sprint string. ['a', 'b', 'c', 'd']
print("Strip spaces:", " Johnson Tyson ".strip())  # Trim whitespaces.

print('Join with spaces', ' '.join(['a', 'b']))


# Slicing  string[start:stop:step].
# start: starting index(inclusive).
# stop: stoping index (exclusive).
# step: How many index to skip (optional)

s = 'Mindshift'
print(s[0:4]) # From index 0 to 3 "Mind"
print(s[:4]) # From index 0 to 3
print(s[4:]) # from index 4 to end "shift"
print(s[-1]) # Last character "t"
print(s[-5:]) # Last 5 characters 'shift'
print(s[::2]) # After every two characters 'Mnsit'
print(s[::-1]) # Reverse string


# Case conversions
leet = 'LeetCode Rocks'
print(leet.lower())
print(leet.upper())
print(leet.capitalize())
print(leet.title())

# Search within strings
mind = 'MindShift'
print(mind.find('Shift'))
print(mind.endswith('Shift'))
print(mind.startswith('r'))

# Replacing content
hi = "hi hi"
print(hi.replace('hi hi', 'Hello World'))

# Length and counting
fruit = 'banana'
print(len(fruit))
print(fruit.count('a'))
print(fruit.count('na'))
print(fruit.count('xaxa'))

# Remove unwanted characters
he = ' hello '
print(he.strip())
print(he.rstrip())
print(he.lstrip())


# Split and join
sentence = 'Hello world'
print(sentence.split())
csv = 'a,b,c,d'
print(csv.split(','))
words = ['mind','shift','rocks']
print("-".join(words))
print('...'.join(words))

# Character check
mix = 'abc1234'
print(mix.isalpha()) # False, contains numbers
print(mix.isalnum()) # True, it contains alphabets and numbers
print(mix.isdigit()) # False
print('1233'.isdigit())
print('abcsd'.isalpha())