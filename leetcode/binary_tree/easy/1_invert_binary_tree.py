"""
Given the root of a binary tree, invert the tree, and return its root.

https://leetcode.com/problems/invert-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution.

    O(...) time complexity
    O(...) space complexity
    """

    def invert_tree(self, root):
        return root


if __name__ == "__main__":
    root = [...]
    instance = Solution()
    print(instance.invert_tree(root))
