# Author: Sakthi Santhosh
# Created on: 31/07/2023
#
# 36 - Valid Sudoku (https://leetcode.com/problems/valid-sudoku/)
def is_valid_sudoku(board: list[list[str]]) -> bool:
    rowmap, columnmap = [set() for _ in range(9)], [set() for _ in range(9)]
    subgridmap = [set() for _ in range(9)]

    for index, row in enumerate(board):
        for subindex, value in enumerate(row):
            if value is '.':
                continue
            if (
                value in rowmap[index]
                or value in columnmap[subindex]
                or value in subgridmap[(index // 3) * 3 + subindex // 3]
            ):
                return False
            rowmap[index].add(value)
            columnmap[subindex].add(value)
            subgridmap[(index // 3) * 3 + subindex // 3].add(value)
    return True

if __name__ == "__main__":
    print(is_valid_sudoku([[]]))
