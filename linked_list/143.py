# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 143 - Reorder List (https://leetcode.com/problems/reorder-list/)
class ListNode:
    def __init__(self, value: int=0, next_node=None) -> None:
        self.value, self.next_node = value, next_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def reorder_list(head_node: ListNode) -> None:
    slow_traverser, fast_traverser = head_node, head_node.next_node

    while fast_traverser and fast_traverser.next_node:
        slow_traverser, fast_traverser = slow_traverser.next_node, fast_traverser.next_node.next_node

    current_node = slow_traverser.next_node
    previous_node = slow_traverser.next_node = None

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node

        previous_node = current_node
        current_node = next_node

    left_node, right_node = head_node, previous_node

    while right_node:
        next_left_node = left_node.next_node
        left_node.next_node = right_node

        next_right_node = right_node.next_node
        right_node.next_node = next_left_node

        left_node = next_left_node
        right_node = next_right_node

if __name__ == "__main__":
    # TODO
    print(reorder_list(ListNode()))
