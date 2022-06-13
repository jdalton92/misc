"""
Given the root of a binary tree, invert the tree, and return its root.

https://leetcode.com/problems/invert-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def list_to_binary_tree(list, index=1):
    # TODO: fix this function
    if not list:
        return None
    mid_num = len(list) // 2
    node = TreeNode(list[mid_num])
    node.left = list_to_binary_tree(list[:mid_num])
    node.right = list_to_binary_tree(list[mid_num + 1 :])
    return node


def print_tree(head):
    if not head:
        return
    print(head.val)
    print_tree(head.left)
    print_tree(head.right)


class RecursiveSolution:
    """Recursive Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def invert_tree(self, root):
        if root is None:
            return None
        left = self.invert_tree(root.left)
        right = self.invert_tree(root.right)
        root.left = right
        root.right = left
        return root


if __name__ == "__main__":
    nums = [4, 2, 7, 1, 3, 6, 9]
    root = list_to_binary_tree(nums)
    instance = RecursiveSolution()
    print_tree(instance.invert_tree(root))
