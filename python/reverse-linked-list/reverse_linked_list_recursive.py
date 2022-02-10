from typing import Optional


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} --> {self.next}"


class Solution:
    def reverse_linked_list_recursively(
        self, head: Optional[Node], prev=None
    ) -> Optional[Node]:
        """
        Reverses a singly-linked-list using recursion.
        In the end returns the last node which becomes the
        new head node.
        """

        if not head:
            return prev

        node = head.next
        head.next = prev

        return self.reverse_linked_list_recursively(node, head)

    def __repr__(self):
        return "Solution to reversing a linked list using recursion"
