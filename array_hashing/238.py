# Author: Sakthi Santhosh
# Created on: 24/07/2023
#
# 1 - Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/)
#
# O(2N) → O(N), O(2N) → O(N)
def product_except_self(nums: list[int]) -> list[int]:
    nums_len = len(nums)
    lprod_array, rprod_array = [1 for _ in range(nums_len)], [1 for _ in range(nums_len)]
    result = []

    for index in range(1, nums_len):
        lprod_array[index] = nums[index - 1] * lprod_array[index - 1]

    for index in range(-2, -nums_len - 1, -1):
        rprod_array[index] = nums[index + 1] * rprod_array[index + 1]

    for index in range(nums_len):
        result.append(lprod_array[index] * rprod_array[index])
    return result

# O(2N) → O(N), O(1)
def product_except_self2(nums: list[int]) -> list[int]:
    cummulative_prod = 1
    result = []

    for num in nums:
        result.append(cummulative_prod)
        cummulative_prod *= num

    cummulative_prod = 1

    for index in range(len(nums) - 1, -1, -1):
        result[index] *= cummulative_prod
        cummulative_prod *= nums[index]

    return result

if __name__ == "__main__":
    print(product_except_self2([1, 2, 3, 4]))
