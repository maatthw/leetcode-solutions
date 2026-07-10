def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

# Time Complexity  : O(n) -> We loop through every number at most
# Space Complexity : O(n) -> seen() can store up to n elements

# Side Note: Technically hash operations have a worst-case of O(n), but insanely unlikely with Python's dict implementation