# Author: Sakthi Santhosh
# Created on: 03/08/2023
#
# 150 - Evaluate Reverse Polish Notation
def eval_rpn(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            stack.append(int(stack.pop(-2) / stack.pop(-1))) # XXX: Avoid // [-7, 2]
        else:
            stack.append(int(token))
    return stack[0]

if __name__ == "__main__":
    print(eval_rpn(
        ['4', "-2", '/', '2', "-3", '-', '-']
    ))
