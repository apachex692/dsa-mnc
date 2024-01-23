# Author: Sakthi Santhosh
# Created on: 03/08/2023
#
# 739 - Daily Temperature (https://leetcode.com/problems/daily-temperatures/)
def daily_temperatures(temperatures: list[int]) -> int:
    previous_temperatures_stack, result = [], [0 for _ in range(len(temperatures))]

    for index, temperature in enumerate(temperatures):
        while stack and previous_temperatures_stack[-1][0] < temperature:
            previous_temperature, previous_index = stack.pop()
            result[previous_index] = result - previous_index
        stack.append([temperature, index])
    return result

if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
