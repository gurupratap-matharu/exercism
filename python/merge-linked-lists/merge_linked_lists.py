"""A utility script to merge two linked lists."""

from typing import Optional


class ListNode:
    """Represents each node of a linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListUtils:
    """Represents a handy class to manipulate linked lists."""

    def merge_two_lists(self, ll_1: Optional[ListNode], ll_2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two already sorted linked lists in ascending order and returns the root node of the sorted list.
        """

        start_node = current_node = ListNode(0)

        while ll_1 and ll_2:
            if ll_1.val < ll_2.val:
                current_node.next = ll_1
                ll_1 = ll_1.next
            else:
                current_node.next = ll_2
                ll_2 = ll_2.next

            current_node = current_node.next

        current_node.next = ll_1 or ll_2

        return start_node.next


if __name__ == '__main__':
    list_1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
    list_2 = ListNode(1, next=ListNode(3, next=ListNode(4)))
    res = LinkedListUtils().merge_two_lists(ll_1=list_1, ll_2=list_2)

    while res:
        print("{}->".format(res.val), end='')
        res = res.next
