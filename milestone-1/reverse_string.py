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