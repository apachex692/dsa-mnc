# Author: Sakthi Santhosh
# Created on: 24/07/2023
#
# 242 - Valid Anagram (https://leetcode.com/problems/valid-anagram/)
def valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_map, s2_map = [0 for _ in range(26)], [0 for _ in range(26)]

    for index in range(len(s1)):
        s1_map[ord(s1[index]) - 97] += 1
        s2_map[ord(s2[index]) - 97] += 1

    for index in range(26):
        if s1_map[index] != s2_map[index]:
            return False
    return True

if __name__ == "__main__":
    print(valid_anagram("anagram", "nagaram"))
