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


def list_to_binary_tree(list, index=1):
    # TODO: fix this function
    if not list:
        return None
    mid_num = len(list) // 2
    node = TreeNode(list[mid_num])
    node.left = list_to_binary_tree(list[:mid_num])
    node.right = list_to_binary_tree(list[mid_num + 1 :])
    return node


class Solution:
    """Solution.

    O(...) time complexity
    O(...) space complexity
    """

    def is_balanced(self, root):
        return root


if __name__ == "__main__":
    nums = [3, 9, 20, None, None, 15, 7]
    root = list_to_binary_tree(nums)
    instance = Solution()
    print(instance.is_balanced(root))
