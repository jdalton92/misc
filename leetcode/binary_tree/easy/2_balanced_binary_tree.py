"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

https://leetcode.com/problems/balanced-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def list_to_binary_tree(list):
    # TODO: fix this function
    if not list:
        return None
    mid_num = len(list) // 2
    node = TreeNode(list[mid_num])
    node.left = list_to_binary_tree(list[:mid_num])
    node.right = list_to_binary_tree(list[mid_num + 1 :])
    return node


class TopDownRecursionSolution:
    """Top down recursion solution.

    O(nlogn) time complexity
    O(n) space complexity
    """

    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def is_balanced(self, root):
        if not root:
            return True

        return (
            abs(self.height(root.left) - self.height(root.right)) < 2
            and self.is_balanced(root.left)
            and self.is_balanced(root.right)
        )


class BottomUpRecursionSolution:
    """Bottom up recursion solution.

    O(n) time complexity
    O(n) space complexity
    """

    def is_balanced_helper(self, root):
        if not root:
            return True, -1

        left_balanced, left_height = self.is_balanced_helper(root.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = self.is_balanced_helper(root.right)
        if not right_balanced:
            return False, 0

        return (abs(left_height - right_height) < 2), 1 + max(left_height, right_height)

    def is_balanced(self, root: TreeNode) -> bool:
        return self.is_balanced_helper(root)[0]


if __name__ == "__main__":
    nums = [3, 9, 20, None, None, 15, 7]
    root = list_to_binary_tree(nums)
    instance = TopDownRecursionSolution()
    print(instance.is_balanced(root))
