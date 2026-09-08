from trees.tree import TreeNode

def isSubtree(root: TreeNode|None, subRoot: TreeNode|None) -> bool:
    def isSameTree(p: TreeNode|None, q: TreeNode|None):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if subRoot is None:
        return True
    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


if __name__ == "__main__":
    root_list = [1,2,3,4,5]
    sub_root_list = [2,4,5]
    root = TreeNode.list_to_tree(root_list)
    subRoot = TreeNode.list_to_tree(sub_root_list)
    print(isSubtree(root, subRoot))

    root_list = [1,2,3,4,5,6,7]
    sub_root_list = [4]
    root = TreeNode.list_to_tree(root_list)
    subRoot = TreeNode.list_to_tree(sub_root_list)
    print(isSubtree(root, subRoot))
