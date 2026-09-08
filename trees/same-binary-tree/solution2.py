from trees.tree import *


def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)




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
