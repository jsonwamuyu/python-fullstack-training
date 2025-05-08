def majority_element(nums):
    """
    Returns the majority element that appears more than len(nums) // 2 times.

    :param nums: List of integers

    :return num: The majority element.
    """

    # Check for an empty list
    if not nums:
        raise ValueError("List can not be empty")

    # This hold the number of count(s) for each element in nums
    counts = {}
    appear_times = len(nums) // 2

    # loop through the nums while updating the counts for each element
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > appear_times:
            return num
    return None


print(majority_element([2]))
print(majority_element([2, 3, 5, 6, 6, 7, 2]))

# majority_element([])
