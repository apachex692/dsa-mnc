# Author: Sakthi Santhosh
# Created on: 07/02/2023
#
# 209 - Minimum Size Subarray Sum (https://leetcode.com/problems/minimum-size-subarray-sum/)
#
# O(N)
def minimum_subarray_sum(target: int, nums: list[int]) -> int:
    start, end, window_sum, len_nums = 0, 0, 0, len(nums)
    min_window = len_nums + 1

    while end < len_nums:
        while window_sum >= target:
            min_window = min(min_window, end - start)
            window_sum -= nums[start]
            start += 1

        window_sum += nums[end]
        end += 1

    while window_sum >= target:
        min_window = min(min_window, end - start)
        window_sum -= nums[start]
        start += 1

    if min_window == len_nums + 1:
        return 0

    return min_window

# O(N)
def minimum_subarray_sum2(target: int, nums: list[int]) -> int:
    start, end, window_sum, len_nums = 0, 0, 0, len(nums)
    min_window = len_nums + 1

    while start < len_nums:
        while window_sum >= target:
            min_window = min(min_window, end - start)
            window_sum -= nums[start]
            start += 1

        if end < len_nums:
            window_sum += nums[end]
            end += 1
        else:
            start += 1

    if min_window == len_nums + 1:
        return 0

    return min_window

# O(N)
def minimum_subarray_sum3(target: int, nums: list[int]) -> int:
    start, end, window_sum, len_nums = 0, 0, 0, len(nums)
    min_window = len_nums + 1

    for end in range(len_nums):
        window_sum += nums[end]

        while window_sum >= target:
            min_window = min(min_window, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return 0 if min_window == len_nums + 1 else min_window

if __name__ == "__main__":
    print(minimum_subarray_sum3(7, [2, 3, 1, 2, 4, 3]))
