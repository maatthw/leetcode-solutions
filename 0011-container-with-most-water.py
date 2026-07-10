def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    # Area will be height x width
        # Height will be min(height[left], height[right]), since the shortest line determines how high up the water can go
        # Width will be (right - left). Simply the difference between the two indices

    while left < right:
        left_height = height[left]
        right_height = height[right]

        area = (right - left) * (min(right_height, left_height))
        max_area = max(max_area, area)

        if left_height < right_height:
            left += 1
        else:
            right -= 1

    return max_area

# Time Complexity  : O(n) -> Need to loop through at most (n-1) elements of the input
# Space Complexity : O(1)
