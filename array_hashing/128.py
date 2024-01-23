# Author: Sakthi Santhosh
# Created on: 31/07/2023
#
# 128 - Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence/)
def longest_consecutive_sequence(nums: list[int]) -> int:
    if nums is []:
        return 0

    nums = set(nums)
    lcs = 0

    for num in nums:
        if num - 1 not in nums:
            counter = 0
            while num + counter in nums:
                counter += 1
            lcs = max(lcs, counter)
    return lcs

if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
