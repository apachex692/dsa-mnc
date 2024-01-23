# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 21 - Merge Two Sorted Lists (https://leetcode.com/problems/merge-two-sorted-lists/)
class ListNode:
    def __init__(self, value: int=0, next_node=None) -> None:
        self.value, self.next_node = value, next_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def merge(self, head_node1: ListNode, head_node2: ListNode) -> ListNode:
    if head_node1 is None:
        return head_node2
    if head_node2 is None:
        return head_node1

    head_node = ListNode()
    last_node = head_node

    while head_node1 and head_node2:
        if head_node1.value <= head_node2.value:
            last_node.next_node = ListNode(val=head_node1.value)
            head_node1 = head_node1.next_node
        else:
            last_node.next_node = ListNode(val=head_node2.value)
            head_node2 = head_node2.next_node

        last_node = last_node.next_node

    last_node.next_node = head_node1 if head_node1 else head_node2
    return head_node.next_node

if __name__ == "__main__":
    # TODO
    print(merge(ListNode(), ListNode()))
