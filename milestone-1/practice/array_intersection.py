def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Returns the intersection of two integer lists with unique elements only.

    This function iterates through nums1 and checks if each element:
    1. Exists in nums2, and
    2. Is not already in the result list (to ensure uniqueness).

    Parameters:
        nums1 (list[int]): First list of integers.
        nums2 (list[int]): Second list of integers.

    Returns:
        list[int]: A list containing the unique intersection of nums1 and nums2.
    """
    inter_list = []

    for n1 in nums1:
        if n1 in nums2 and n1 not in inter_list:
            inter_list.append(n1)

    return inter_list
