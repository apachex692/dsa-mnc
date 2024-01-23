# Author: Sakthi Santhosh
# Created on: 11/08/2023
#
# 875 - Koko Eating Bananas (https://leetcode.com/problems/koko-eating-bananas/)
from math import ceil

def min_eating_speed(piles: list[int], hours: int) -> int:
    left, right = 1, max(piles)
    result = right

    while left <= right:
        middle, hours_curr = (left + right) // 2, 0

        for pile in piles:
            hours_curr += ceil(pile / middle)

        print(middle, hours_curr)

        if hours_curr > hours:
            left = middle + 1
        elif hours_curr < hours:
            result += min(result, middle)
            right = middle - 1
    return result

if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))
