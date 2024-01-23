# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 2 - Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)
class ListNode:
    def __init__(self, value: int=0, next_node=None) -> None:
        self.value, self.next_node = value, next_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def add_two_nums(head_node1: ListNode, head_node2: ListNode) -> ListNode:
    dummy_head_node = ListNode()
    current_node, carry = dummy_head_node, 0

    while head_node1 or head_node2 or carry:
        total = (head_node1.value if head_node1 else 0) + (head_node2.value if head_node2 else 0) + carry
        carry = total // 10

        current_node.next_node = ListNode(total % 10)
        current_node = current_node.next_node

        if head_node1:
            head_node1 = head_node1.next_node
        if head_node2:
            head_node2 = head_node2.next_node
    return dummy_head_node.next_node

if __name__ == "__main__":
    # TODO
    print(add_two_nums(ListNode(), ListNode()))
