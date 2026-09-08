from typing import Optional

from trees.tree import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None: return None

    queue = [root]
    for node in queue:
        if node:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            node.left, node.right = node.right, node.left

    return root


if __name__ == "__main__":
    t3 = TreeNode(1)
    t2 = TreeNode(2)
    t1 = TreeNode(3, t2, t3)
    t1.print_tree()
    invert_t1 = invertTree(t1)
    invert_t1.print_tree() if invert_t1 else None
