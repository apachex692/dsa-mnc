# Author: Sakthi Santhosh
# Created on: 12/08/2023
#
# 153 - Find Minimum in Rotated Sorted Array (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
def find_minimum(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    result = nums[0]

    while left <= right:
        middle = (left + right) // 2

        if nums[left] <= nums[middle]:
            result = min(result, nums[left])
            left = middle + 1
        else:
            result = min(result, nums[middle])
            right = middle - 1
    return result

if __name__ == "__main__":
    print(find_minimum([4, 5, 6, 7, 0, 1, 2]))
