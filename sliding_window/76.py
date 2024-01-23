# Author: Sakthi Santhosh
# Created on: 02/08/2023
#
# 76 - Minimum Window Substring (https://leetcode.com/problems/minimum-window-substring/)
def min_window(string1: str, string2: str) -> str:
    if string2 == "":
        return ""

    string2_countmap, string1_window_countmap = {}, {}
    len_min, len_min_indices = float("infinity"), [-1, -1]
    left, matches = 0, 0

    for character in string2:
        string2_countmap[character] = 1 + string2_countmap.get(character, 0)

    for right in range(len(string1)):
        string1_window_countmap[string1[right]] = 1 + string1_window_countmap.get(string1[right], 0)

        if (
            string1[right] in string2
            and string1_window_countmap[string1[right]] == string2_countmap[string1[right]]
        ):
            matches += 1

        while matches == len(string2_countmap):
            if right - left + 1 < len_min:
                len_min = right - left + 1
                len_min_indices = [left, right]

            string1_window_countmap[string1[left]] -= 1
            if (
                string1[left] in string2
                and string1_window_countmap[string1[left]] < string2_countmap[string1[left]]
            ):
                matches -= 1

            left += 1
    return (
        string1[len_min_indices[0]: len_min_indices[1] + 1]
        if len_min != float("infinity")
        else ""
    )

if __name__ == "__main__":
    print(min_window("aa", "aa"))
