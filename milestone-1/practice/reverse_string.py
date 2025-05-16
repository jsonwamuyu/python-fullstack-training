import itertools

def reverse_string(s):
    """
    Reverses the input list of characters in-place.

    Parameters:
        s (List[str]): A list of characters to reverse.

    Returns:
        None: The list is modified in-place.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters at left and right indices
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

john = ['j','o','h','n']
reverse_string(john)
print(john) # ['n', 'h', 'o', 'j']






# comparing two strings using zip(s1, s2) method in parallel
def compare_string(s1, s2):
    if len(s1) != len(s2):
        # We use itertools.zip_longest() to handle missing letters
        for l1, l2 in itertools.zip_longest(s1, s2):
            print(f'{l1} - {l2}')

    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            print(f'{c1} == {c2}')
        else:
            print(f'{c1} != {c2}')

# compare_string('Hello', 'ZeLlpooo')



print(ord('a'))