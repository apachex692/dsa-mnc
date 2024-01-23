# Author: Sakthi Santhosh
# Created on: 15/08/2023
#
# 206 - Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/)
class ListNode:
    def __init__(self, value: int=0, next_node=None) -> None:
        self.value, self.next_node = value, next_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def reverse(head_node: ListNode) -> ListNode:
    if head_node is None:
        return None

    previous_node, current_node = None, head_node

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node

        previous_node = current_node
        current_node = next_node
    return previous_node

if __name__ == "__main__":
    # TODO
    print(reverse(ListNode()))
