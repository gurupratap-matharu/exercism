from typing import List, Optional

from node import Node


class Traverse:
    def traverse_iteratively(self, head: Optional[Node]) -> Optional[List]:
        """
        Traverses a singly linked list iteratively and returns a list
        of all node values.
        """

        LL = []

        while head:
            LL.append(head.value)
            head = head.next

        return LL

    def traverse_recursively(self, head: Optional[Node]) -> Optional[List]:
        """
        Traverses a singly linked list recursively and returns a list
        of all node values.
        """

        if not head:
            return []

        return [head.value] + self.traverse_recursively(head.next)


if __name__ == "__main__":
    head = Node(value=1, next=Node(value=2, next=Node(value=3)))

    print(Traverse().traverse_recursively(head))
    print(Traverse().traverse_iteratively(head))
