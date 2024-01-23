# Author: Sakthi Santhosh
# Created on: 23/08/2023
#
# 138 - Copy List with Random Pointer (https://leetcode.com/problems/copy-list-with-random-pointer/)
class ListNode:
    def __init__(self, value: int=0, next_node=None, random_node=None) -> None:
        self.value = value
        self.next_node, self.random_node = next_node, random_node

    def __repr__(self) -> str:
        return f"<ListNode {self.value}>"

def deep_copy(head_node: ListNode) -> ListNode:
    if head_node is None:
            return None

    new_head_node = ListNode(val=head_node.value)
    previous_node, traverser_node = new_head_node, head_node.next_node
    hashmap = {head_node: new_head_node}

    while traverser_node:
        new_node = ListNode(val=traverser_node.value)
        hashmap[traverser_node] = new_node

        previous_node.next_node = new_node
        previous_node = new_node
        traverser_node = traverser_node.next_node

    traverser_node, new_traverser_node = head_node, new_head_node

    while traverser_node:
        if traverser_node.random is None:
            new_traverser_node.random = None
        else:
            new_traverser_node.random = hashmap[traverser_node.random]

        traverser_node, new_traverser_node = traverser_node.next_node, new_traverser_node.next_node
    return new_head_node

if __name__ == "__main__":
    # TODO
    print(deep_copy(ListNode()))
