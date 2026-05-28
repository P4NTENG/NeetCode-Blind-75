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
    dummy = ListNode()
    curr = dummy

    while curr and head:
        tail_1 = head
        while tail_1 and tail_1.next and tail_1.next.next:
            tail_1 = tail_1.next
        tail = tail_1.next
        tail_1.next = None

        curr.next = head
        curr = curr.next
        head = head.next
        curr.next = tail
        curr = curr.next


list1 = [2, 4, 6, 8, 10]

list1_head = build(list1)

printList(list1_head)
reorderList(list1_head)
printList(list1_head)

list1 = [2]

list1_head = build(list1)

printList(list1_head)
reorderList(list1_head)
printList(list1_head)
