# Author: Sakthi Santhosh
# Created on: 01/08/2023
#
# 42 - Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/)
def trap(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    l_max, r_max = 0, 0
    water = 0

    while left < right:
        if heights[left] < heights[right]:
            l_max = max(l_max, heights[left])
            water += l_max - heights[left]
            left += 1
        else:
            r_max = max(r_max, heights[right])
            water += r_max - heights[right]
            right -= 1
    return water

if __name__ == "__main__":
    print(trap([]))
