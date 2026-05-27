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
    head = list1
    curr1, curr2 = list1, list2

    while curr1 and curr2:
        if curr1.val < curr2.val:
            next_node = curr1.next
            curr1.next = curr2
            curr1 = next_node
        else:
            next_node = curr2.next
            curr2.next = curr1
            curr2 = next_node

    return head


list1 = [1, 2, 4]
list2 = [1, 3, 5]

list1_head = build(list1)
list2_head = build(list2)

printList(list1_head)
printList(list2_head)

list3_head = mergeTwoLists(list1_head, list2_head)

printList(list3_head)
