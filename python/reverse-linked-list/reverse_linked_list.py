from typing import Optional


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[Node]) -> Optional[Node]:
        """
        Reverses a singly-linked list. That's it
        """

        node = head
        prev = None

        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        return prev
