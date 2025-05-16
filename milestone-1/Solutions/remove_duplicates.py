def remove_duplicates(nums):
    # Iterate through the list in reverse order deleting any repeated number from the list.
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i - 1]
    return len(nums)


print(remove_duplicates([1, 3, 4, 4, 4]))
