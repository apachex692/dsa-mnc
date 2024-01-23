# Author: Sakthi Santhosh
# Created on: 01/08/2023
#
# 11 - Container with Most Water (https://leetcode.com/problems/container-with-most-water/)
def max_area(heights: list[int]) -> int:
    a_max = 0
    left, right = 0, len(heights) - 1

    while left < right:
        h_min = min(heights[left], heights[right])
        a_max = max(a_max, h_min * (right - left))

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return a_max

if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
