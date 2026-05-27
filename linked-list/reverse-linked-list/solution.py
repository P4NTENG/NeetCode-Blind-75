# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr:
        if curr.next:
            next_node = curr.next
            prev = curr
            curr = prev.next
            curr.next = prev

    return
