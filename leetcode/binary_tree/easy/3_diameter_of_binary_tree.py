"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

https://leetcode.com/problems/diameter-of-binary-tree/
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


class Solution:
    """Solution.

    O(n) time complexity
    O(n) space complexity
    """

    max_diameter = 0

    def height(self, root):
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        self.max_diameter = max(self.max_diameter, left_height + right_height)

        # Add 1 for path connecting the node and its parent
        return 1 + max(left_height, right_height)

    def diameter_of_binary_tree(self, root):
        self.height(root)
        return self.max_diameter


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    root = list_to_binary_tree(nums)
    instance = Solution()
    print(instance.diameter_of_binary_tree(root))
