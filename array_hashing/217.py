# Author: Sakthi Santhosh
# Created on: 24/07/2023
#
# 217 - Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)
def contains_duplicate(nums: list[int]) -> bool:
    visited = set()

    for num in nums:
        if num in visited:
            return True
        visited.add(num)
    return False

if __name__ == "__main__":
    contains_duplicate([1, 2, 3])
