# Author: Sakthi Santhosh
# Created on: 02/08/2023
#
# 20 - Valid Parenthesis (https://leetcode.com/problems/valid-parentheses/)
def is_matching_pair(open_bracket, close_bracket):
    return (
        (open_bracket == '(' and close_bracket == ')')
        or (open_bracket == '{' and close_bracket == '}')
        or (open_bracket == '[' and close_bracket == ']')
    )

def is_valid(string: str) -> bool:
    stack = []

    for character in string:
        if character in ('(', '{', '['):
            stack.append(character)
        elif character in (')', '}', ']'):
            if not len(stack) or not is_matching_pair(stack[-1], character):
                return False
            stack.pop()
    return not len(stack)

if __name__ == "__main__":
    print(is_valid("[]"))
