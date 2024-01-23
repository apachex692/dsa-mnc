# Author: Sakthi Santhosh
# Created on: 07/08/2023
#
# 853 - Car Fleet (https://leetcode.com/problems/car-fleet/)
def car_fleet(target: int, positions: list[int], speeds: list[int]) -> int:
    pairs = sorted(
        [[position, speed] for position, speed in zip(positions, speeds)],
        reverse=True
    )
    fleet_stack = []

    fleet_stack.append((target - pairs[0][0]) / pairs[0][1])
    for position, speed in pairs[1:]:
        fleet_stack.append((target - position) / speed)

        if fleet_stack[-1] <= fleet_stack[-2]:
            fleet_stack.pop()
    return len(fleet_stack)

if __name__ == "__main__":
    print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
