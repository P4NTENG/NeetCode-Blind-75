from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(arr: list) -> Optional[ListNode]:

    head = None

    for num in reversed(arr):
        head = ListNode(num, head)

    return head


def printList(head: Optional[ListNode]):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


def reorderList(head: Optional[ListNode]) -> None:
    slow = head
    fast = head

    while slow and fast and slow.next and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow.next if slow else None
    if slow:
        slow.next = None

    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    tail = reverseList(middle)
    next1 = next2 = None
    curr = head

    while curr and head and tail:
        next1 = head.next
        next2 = tail.next

        curr.next = next1
        next1 = next1.next
        curr = curr.next
        head.next = next2
        next2 = next2.next
        head = head.next


list1 = [2, 4, 6, 8, 10]

list1_head = build(list1)

printList(list1_head)
reorderList(list1_head)
printList(list1_head)
