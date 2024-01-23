# Author: Sakthi Santhosh
# Created on: 02/08/2023
#
# 239 - Sliding Window Maximum (https://leetcode.com/problems/sliding-window-maximum/)
def max_sliding_window(nums: list[int], window_size: int) -> list[int]:
    from collections import deque

    indices_deque, result = deque(), []
    left = 0

    for right in range(len(nums)):
        while indices_deque and nums[indices_deque[-1]] < nums[right]:
            indices_deque.pop()
        indices_deque.append(right)

        if left > indices_deque[0]: # [1, -1], 1
            indices_deque.popleft()

        if right  + 1 >= window_size:
            result.append(nums[indices_deque[0]])
            left += 1
    return result

if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 1))
