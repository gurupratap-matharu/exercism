class Node:
    """Generic Node which has a value and a pointer to a next node"""

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} --> {self.next}"
