# Author: Sakthi Santhosh
# Created on: 01/08/2023
#
# 424 - Longest Repeating Character Replacement (https://leetcode.com/problems/longest-repeating-character-replacement/)
#
# O(26N), O(N)
def character_replacement(string: str, chances: int) -> int:
    window_max, countmap = 0, {}
    left = 0

    for right in range(len(string)):
        countmap[string[right]] = 1 + countmap.get(string[right], 0)

        while (right - left + 1) - max(countmap.values()) > chances:
            countmap[string[left]] -= 1
            left += 1
        window_max = max(window_max, right - left + 1)
    return window_max

# O(N), O(N)
def character_replacement2(string: str, chances: int) -> int:
    window_max, charcount_max = 0, 0
    countmap = {}
    left = 0

    for right in range(len(string)):
        countmap[string[right]] = 1 + countmap.get(string[right], 0)
        charcount_max = max(charcount_max, countmap[string[right]])

        while (right - left + 1) - charcount_max > chances:
            countmap[string[left]] -= 1
            left += 1
        window_max = max(window_max, right - left + 1)
    return window_max

if __name__ == "__main__":
    print(character_replacement2("AABABBA", 1))
