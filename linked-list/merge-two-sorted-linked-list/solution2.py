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


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    smaller, bigger = list1, list2
    head = None
    if smaller and bigger and smaller.val >= bigger.val:
        head = smaller
    while smaller and bigger:
        if smaller.val >= bigger.val:
            smaller, bigger = bigger, smaller
        next_node = smaller.next
        smaller.next = min(bigger.val, next_node.val if next_node else float("inf"))
        smaller = next_node

    return head


list1 = [1, 2, 4]
list2 = [1, 3, 5]

list1_head = build(list1)
list2_head = build(list2)

printList(list1_head)
printList(list2_head)

list3_head = mergeTwoLists(list1_head, list2_head)

printList(list3_head)
