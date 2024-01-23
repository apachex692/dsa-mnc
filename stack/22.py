# Author: Sakthi Santhosh
# Created on: 03/08/2023
#
# 22 - Generate Parentheses (https://leetcode.com/problems/generate-parentheses/)
def generate_parentheses_wrapper(brackets: int) -> list[str]:
    bracket_stack, result = [], []

    def generate_parentheses(open_bracket_count, close_bracket_count):
        if open_bracket_count == close_bracket_count == brackets:
            result.append("".join(bracket_stack))
            return

        if open_bracket_count < brackets:
            bracket_stack.append('(')
            generate_parentheses(open_bracket_count + 1, close_bracket_count)
            bracket_stack.pop()

        if close_bracket_count < open_bracket_count:
            bracket_stack.append(')')
            generate_parentheses(open_bracket_count, close_bracket_count + 1)
            bracket_stack.pop()

    generate_parentheses(0, 0)
    return result

if __name__ == "__main__":
    print(generate_parentheses_wrapper(3))
