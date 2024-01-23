# Author: Sakthi Santhosh
# Created on: 02/08/2023
#
# 567 - Permutation in String (https://leetcode.com/problems/permutation-in-string/)
def check_inclusion(string1: str, string2: str) -> bool:
    if len(string1) > len(string2):
        return False

    countmap1, countmap2 = [0 for _ in range(26)], [0 for _ in range(26)]
    left, matches = 0, 0

    for index in range(len(string1)):
        countmap1[ord(string1[index]) - 97] += 1
        countmap2[ord(string2[index]) - 97] += 1

    for index in range(26):
        matches += (countmap1[index] == countmap2[index])

    for right in range(len(string1), len(string2)):
        if matches == 26:
            return True

        countmap_index_right = ord(string2[right]) - 97
        countmap2[countmap_index_right] += 1

        if countmap2[countmap_index_right] == countmap1[countmap_index_right]:
            matches += 1
        elif countmap2[countmap_index_right] == countmap1[countmap_index_right] + 1:
            matches -= 1

        countmap_index_left = ord(string2[left]) - 97
        countmap2[countmap_index_left] -= 1

        if countmap2[countmap_index_left] == countmap1[countmap_index_left]:
            matches += 1
        elif countmap2[countmap_index_left] == countmap1[countmap_index_left] - 1:
            matches -= 1
        left += 1
    return matches == 26

if __name__ == "__main__":
    print(check_inclusion("ab", "eidboaoo"))
