# Author: Sakthi Santhosh
# Created on: 01/08/2023
#
# 3 - Longest Substring without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
def length_of_longest_substring(string: str) -> int:
    left, len_max = 0, 0
    visited = {}

    for right in range(len(string)):
        if string[right] in visited:
            left = max(left, visited[string[right]] + 1)

        visited[string[right]] = right
        len_max = max(len_max, right - left + 1)
    return len_max

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
