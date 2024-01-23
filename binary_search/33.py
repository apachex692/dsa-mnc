# Author: Sakthi Santhosh
# Created on: 14/08/2023
#
# 33 - Search in Rotated Sorted Array (https://leetcode.com/problems/search-in-rotated-sorted-array/)
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        if nums[left] <= nums[middle]:
            if nums[left] <= target and target <= nums[middle]:
                right = middle
            else:
                left = middle + 1
        else:
            if nums[middle] <= target and target <= nums[right]:
                left = middle
            else:
                right = middle - 1
    return -1

if __name__ == "__main__":
    print(search([], 0))
