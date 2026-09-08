from trees.tree import *


def maxDepth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    left = maxDepth(root.left if root else None)
    right = maxDepth(root.right if root else None)
    return max(left, right) + 1


if __name__ == "__main__":
    node_list = [1, 2, 3, None, None, 4]
    root = TreeNode.list_to_tree(node_list)

    print(maxDepth(root))
