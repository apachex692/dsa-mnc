# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 287 - Find the Duplicate Number (https://leetcode.com/problems/find-the-duplicate-number/)
def find_duplicate(nums: list[int]) -> int:
    slow_pointer = fast_pointer = 0

    while True:
        slow_pointer, fast_pointer = nums[slow_pointer], nums[nums[fast_pointer]]

        if slow_pointer == fast_pointer:
            break

    slow_pointer = 0

    while True:
        slow_pointer, fast_pointer = nums[slow_pointer], nums[fast_pointer]

        if slow_pointer == fast_pointer:
            return slow_pointer

if __name__ == "__main__":
    print(find_duplicate([]))
