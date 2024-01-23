# Author: Sakthi Santhosh
# Created on: 24/07/2023
#
# 217 - Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/)
def topk_frequent(nums: list[int], k: int) -> list[int]:
    countmap = {}
    sorted_list = [[] for _ in range(len(nums) + 1)]
    result = []

    for num in nums:
        if num in countmap:
            countmap[num] += 1
        else:
            countmap[num] = 1

    for num in countmap:
        sorted_list[countmap[num]].append(num)

    for index in range(-1, -len(nums) - 1, -1):
        for num in sorted_list[index]:
            result.append(num)
            if len(result) == k:
                return result

if __name__ == "__main__":
    print(topk_frequent([1], 1))
