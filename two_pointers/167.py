# Author: Sakthi Santhosh
# Created on: 31/07/2023
#
# 167 - Two Sum II - Input Array is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
def two_sum(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left + 1, right + 1]

if __name__ == "__main__":
    print(two_sum([2, 3, 4], 6))
