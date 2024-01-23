# Author: Sakthi Santhosh
# Created on: 10/08/2023
#
# 74 - Search a 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/)
def search(matrix: list[list[int]], target: int) -> bool:
    top, bottom = 0, len(matrix) - 1

    while top <= bottom:
        middle_row = (top + bottom) // 2

        if matrix[middle_row][0] > target:
            bottom = middle_row - 1
        elif matrix[middle_row][-1] < target:
            top = middle_row + 1
        else:
            break

    if not top <= bottom:
        return False

    left, right = 0, len(matrix[0]) - 1

    while left <= right:
        middle_column = (left + right) // 2

        if matrix[middle_row][middle_column] > target:
            right = middle_column - 1
        elif matrix[middle_row][middle_column] < target:
            left = middle_column + 1
        else:
            return True
    return False

if __name__ == "__main__":
    print(search([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], -1))
