# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 141 - Linked List Cycle (https://leetcode.com/problems/linked-list-cycle/)
class ListNode:
    def __init__(self, value: int=0, next_node=None) -> None:
        self.value, self.next_node = value, next_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def has_cycle(head_node: ListNode) -> bool:
    tortoise = hare = head

    while hare and hare.next_node:
        tortoise, hare = tortoise.next_node, hare.next_node.next_node

        if hare == tortoise:
            return True
    return False

if __name__ == "__main__":
    # TODO
    print(has_cycle(ListNode()))
