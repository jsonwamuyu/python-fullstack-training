def two_sum(nums: list[int], target: int) -> list[int]:
    # Enumerate through the list to produce a key and value pair
    # this will help keep track of the indexes
    for key, value in enumerate(nums):
        # Take target and minus the current value then
        # check whether this value exist in the list (nums).
        # if it does, return both indexes of current key and value
        no_wanted = target - value
        if no_wanted in nums[key + 1 :]:
            # print('Found it:', no_wanted)
            return [key, nums.index(no_wanted)]

    return ValueError("No match found")


print(two_sum([2, 4, 3], 7))
print(two_sum([1, 2], 3))
print(two_sum([2, 3], 1))
