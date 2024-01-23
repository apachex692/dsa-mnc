# Author: Sakthi Santhosh
# Created on: 24/07/2023
#
# 49 - Group Anagrams (https://leetcode.com/problems/group-anagrams/)
def group_anagrams(strings: list[str]) -> list[list[str]]:
    hashmap = {} # tuple[int] -> list[str]

    for string in strings:
        countmap = [0] * 26

        for char in string:
            countmap[ord(char) - 97] += 1

        if tuple(countmap) in hashmap:
            hashmap[tuple(countmap)].append(string)
        else:
            hashmap[tuple(countmap)] = [string]
    return hashmap.values()

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
