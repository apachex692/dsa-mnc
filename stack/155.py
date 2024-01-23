# Author: Sakthi Santhosh
# Created on: 03/08/2023
#
# 155 - Min Stack (https://leetcode.com/problems/min-stack/)
class MinStack:
    def __init__(self) -> None:
        self.stack, self.stack_min = [], []

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.stack_min.append(
            min(value, self.stack_min[-1] if self.stack_min else value)
        )

    def pop(self) -> None:
        del self.stack_min[-1], self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.stack_min[-1]

if __name__ == "__main__":
    pass
