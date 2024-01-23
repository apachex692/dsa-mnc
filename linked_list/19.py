# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 19 - Remove Nth Node from End of List (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
class ListNode:
    def __init__(self, value: int=0, next_node=None) -> None:
        self.value, self.next_node = value, next_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def remove_node(head_node: ListNode) -> ListNode:
    previous_node, current_node, fast_traverser = None, head_node, head_node

    for _ in range(n):
        fast_traverser = fast_traverser.next_node

    if not fast_traverser:
        return head_node.next_node

    while fast_traverser:
        previous_node = current_node
        current_node = current_node.next_node
        fast_traverser = fast_traverser.next_node

    previous_node.next_node = current_node.next_node
    return head_node

if __name__ == "__main__":
    # TODO
    print(remove_node(ListNode()))
