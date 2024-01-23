# Author: Sakthi Santhosh
# Created on: 15/08/2023
#
# 981 - Time Based Key-value Store (https://leetcode.com/problems/time-based-key-value-store/)
class TimeMap:
    def __init__(self) -> None:
        self._time_map = {}

    def setter(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._time_map:
            self._time_map[key] = []

        self._time_map[key].append((value, timestamp))

    def getter(self, key: str, timestamp: str) -> str:
        values = self._time_map.get(key, None)

        if values is None:
            return ""

        result = ""
        left, right = 0, len(values) - 1

        while left <= right:
            middle = (left + right) // 2

            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return result

if __name__ == "__main__":
    time_map = TimeMap()
    # TODO
