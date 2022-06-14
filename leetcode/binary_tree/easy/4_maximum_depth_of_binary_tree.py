"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
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


class RecursiveSolution:
    """Recursive Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def max_depth(self, root):
        return self.height(root)


class IterativeSolution:
    """Iterative solution.

    O(n) time complexity
    O(logn) space complexity (average case ie. nodes are balanced, therefore height of
    BST is logn)
    O(n) space complexity (worse case ie. nodes all in 1 direction)
    """

    def max_depth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth


if __name__ == "__main__":
    nums = [3, 9, 20, None, None, 15, 7]
    root = list_to_binary_tree(nums)
    instance = RecursiveSolution()
    print(instance.max_depth(root))
