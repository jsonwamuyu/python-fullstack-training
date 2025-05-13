"""
TUPLE

Ordered, immutable collection. Once created, can not be changed( can not add, delete,or modify)
Its like a list but immutable.

(,)
"""

# Creating tuple
tuple_one = ()  # Empty tuple
tuple_two = ("one",)  # Singleton tuple -> must include a comma
kenyan_citizen = ("Alice Mwikali", 32132133, "Female", 34)


# Accessing tuple
print("Citizen details:", kenyan_citizen[1])

# Slicing
print("slice(0 to 2 excluded):", kenyan_citizen[0:2])
print("Copy(Shallow) everything:", kenyan_citizen[:])


# Length
print("Length of the tuple:", len(kenyan_citizen))


# Iteration
for item in kenyan_citizen:
    print(item)


# Nested tuples
nested_tuple = (1, 2, (3, 4), 5, 6)
print("Nested tuple:", nested_tuple[2][1])  # Prints 4 in (3,4)


print("An empty tuple:", tuple_one)
for n in tuple_one:
    print(n)


# Return multiple values from function
def get_person():
    """Return multiple values - name, age"""
    return ("Alice",)


print("Person details:", get_person())


"""
Problem:

Write a function that takes a list of tuples like: 
students = [("John", 82), ("Alice", 91), ("Bob", 78)].
And returns the name of the student with the highest score.
"""
def student_highest_score(students):
    # Holds all the scores
    scores = []
    if len(students) == 0:
        return None

    for student in students:
        scores.append((student[1], student[0]))

    # Sort the scores and then return the highest
    sorted_scores = sorted(scores)

    # extract the highest score, which is the last in the sorted list
    highest_score = sorted_scores[-1]
    return highest_score[1]

highest = student_highest_score([('Alice',45), ('Mike',30), ('Nick', 12), ('Jeff',50)])
print(highest)