# Author: Sakthi Santhosh
# Created on: 08/02/2024
#
# 16 - 3Sum Closest (https://leetcode.com/problems/3sum-closest/)
def threeSumClosest(self, nums: list[int], target: int) -> int:
    len_nums = len(nums)

    if len(nums) == 3:
        return sum(nums)

    min_diff, sum_closest = float("inf"), 0

    nums.sort()
    for index in range(len_nums - 2):
        left, right = index + 1, len_nums - 1

        while left < right:
            total = nums[index] + nums[left] + nums[right]
            difference = abs(total - target)

            if target == total:
                return target

            if difference < min_diff:
                min_diff = difference
                sum_closest = total

            if total > target:
                right -= 1
            else:
                left += 1

    return sum_closest
