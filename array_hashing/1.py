# Author: Sakthi Santhosh
# Created on: 24/07/2023
#
# 1 - Two Sum (https://leetcode.com/problems/two-sum/)
def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for index, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], index]
        hashmap[num] = index

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
