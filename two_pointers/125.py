# Author: Sakthi Santhosh
# Created on: 31/07/2023
#
# 125 - Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)
def is_palindrome(string: str) -> bool:
    left, right = 0, len(string) - 1

    while left < right:
        if not string[left].isalnum():
            left += 1
        elif not string[right].isalnum():
            right -= 1
        else:
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
    return True

if __name__ == "__main__":
    print(is_palindrome("0P"))
