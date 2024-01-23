# Author: Sakthi Santhosh
# Created on: 01/08/2023
#
# 15 - 3Sum (https://leetcode.com/problems/3sum/)
def three_sum(nums: list[int]) -> list[int]:
    triplets = []
    nums_len = len(nums)

    nums.sort()
    for index in range(nums_len - 2):
        if index and nums[index] == nums[index - 1]:
            continue

        left, right = index + 1, nums_len - 1

        while left < right:
            if nums[index] + nums[left] + nums[right] == 0:
                triplets.append([nums[index], nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif nums[index] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                left += 1
    return triplets

if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, 4]))
