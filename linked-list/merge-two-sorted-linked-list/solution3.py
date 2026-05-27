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
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    else:
        smaller, bigger = list1, list2
        head = bigger if smaller and bigger and smaller.val >= bigger.val else smaller

        while smaller and bigger:
            if smaller.val >= bigger.val:
                smaller, bigger = bigger, smaller
            next_node = smaller.next
            if next_node is None or next_node.val >= bigger.val:
                smaller.next = bigger
            smaller = next_node

        return head


list1 = [1, 2]
list2 = [1, 3]

list1_head = build(list1)
list2_head = build(list2)

printList(list1_head)
printList(list2_head)

list3_head = mergeTwoLists(list1_head, list2_head)

printList(list3_head)

# expect 1 1 2 3
