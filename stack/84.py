# Author: Sakthi Santhosh
# Created on: 09/08/2023
#
# 84 - Largest Rectangle in Histogram (https://leetcode.com/problems/largest-rectangle-in-histogram/)
def largest_rectangle_area(heights: list[int]) -> int:
    stack, area_max = [], 0

    for index, height in enumerate(heights):
        start = index

        while stack and stack[-1][1] > height:
            curr_index, curr_height = stack.pop()
            area_max = max(area_max, curr_height * (index - curr_index))
            start = curr_index
        stack.append((start, height))

    for index, height in stack:
        area_max = max(area_max, height * (len(heights) - index))
    return area_max

if __name__ == "__main__":
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
