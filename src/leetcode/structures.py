"""Module defining stuctures used throughout the solutions."""


class ListNode:
    """Representation of a linked list."""

    def __init__(self, val=0, next=None):
        """Define the node payload and pointer to next node."""
        self.val = val
        self.next = next

    def has_next(self) -> bool:
        """Check the existence of a next node."""
        return self.next is None

    def __eq__(self, other):
        """Check values and next node are the same."""
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        """Print the list."""
        return f"{self.val}, {self.next}"
