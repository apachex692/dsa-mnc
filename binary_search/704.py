# Author: Sakthi Santhosh
# Created on: 10/08/2023
#
# 704 - Binary Search (https://leetcode.com/problems/binary-search/)
def search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 2))
