# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 146 - LRU Cache (https://leetcode.com/problems/lru-cache/)
class DLListNode:
    def __init__(self, key: int=0, value: int=0, previous_node=None, next_node=None):
        self.key, self.value = key, value
        self.previous_node, self.next_node = previous_node, next_node

    def __repr__(self):
        return f"{self.key, self.value, id(self)}"

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hashmap = {}

        self._head_node, self._tail_node = DLListNode(), DLListNode()
        self._head_node.next_node, self._tail_node.previous_node = self._tail_node, self._head_node

    def get(self, key: int) -> int:
        if key not in self._hashmap:
            print()
            return -1
        if self._hashmap[key] == self._head_node.next_node:
            return self._hashmap[key].value

        tbd_node = self._hashmap[key]
        tbd_node.previous_node.next_node = tbd_node.next_node
        tbd_node.next_node.previous_node = tbd_node.previous_node

        return_value = tbd_node.value
        new_node = DLListNode(key=tbd_node.key, value=tbd_node.value)
        self._hashmap[key] = new_node

        del tbd_node
        self._mru(new_node)
        return return_value

    def put(self, key: int, value: int) -> None:
        if key in self._hashmap:
            node = self._hashmap[key]
            node.value = value

            node.previous_node.next_node = node.next_node
            node.next_node.previous_node = node.previous_node

            self._mru(node)
        elif self._capacity == 0:
            tbd_node = self._tail_node.previous_node
            tbd_node.previous_node.next_node = self._tail_node

            self._tail_node.previous_node = tbd_node.previous_node
            self._capacity += 1

            self._hashmap.pop(tbd_node.key)
            del tbd_node
            self.put(key, value)
        else:
            self._capacity -= 1
            new_node = DLListNode(key=key, value=value)
            self._hashmap[key] = new_node

            self._mru(new_node)

    def _mru(self, node: ListNode) -> None:
        head_next_node = self._head_node.next_node

        self._head_node.next_node = node
        node.next_node = head_next_node

        head_next_node.previous_node = node
        node.previous_node = self._head_node

if __name__ == "__main__":
    # TODO
    lru_ds = LRUCache(capacity=0)
    # TODO
