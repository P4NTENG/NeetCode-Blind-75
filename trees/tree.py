class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_val(self):
        print(self.val)

    def print_tree(self):
        queue = [self]
        for node in queue:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node.val)

    @staticmethod
    def list_to_tree(num_list: list[int]) -> "TreeNode":
        node_list = [TreeNode(x) for x in num_list]
        root = node_list[0]

        for idx, node in enumerate(node_list):
            node.left = node_list[2 * idx + 1] if 2 * idx + 1 < len(num_list) else None
            node.right = node_list[2 * idx + 2] if 2 * idx + 2 < len(num_list) else None

        return root


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t1 = TreeNode.list_to_tree(l1)
    t1.print_tree()
