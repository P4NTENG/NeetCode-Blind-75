from collections import deque

from trees.tree import *


def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    p_queue = deque()
    q_queue = deque()
    p_queue.append(p)
    q_queue.append(q)

    while p_queue and q_queue:
        p_curr = p_queue.popleft()
        q_curr = q_queue.popleft()

        if p_curr is None and q_curr is None:
            continue
        if p_curr is None or q_curr is None:
            return False
        if p_curr.val != q_curr.val:
            return False

        p_queue.append(p_curr.left)
        p_queue.append(p_curr.right)
        q_queue.append(q_curr.left)
        q_queue.append(q_curr.right)

    return True


if __name__ == "__main__":
    p_list = [1, None, 3, 4]
    q_list = [1, None, 3, 4]
    p = TreeNode.list_to_tree(p_list)
    q = TreeNode.list_to_tree(q_list)
    print(isSameTree(p, q))
    p_list = [1, 3, 3, 4]
    q_list = [1, 3, 3]
    p = TreeNode.list_to_tree(p_list)
    q = TreeNode.list_to_tree(q_list)
    print(isSameTree(p, q))
