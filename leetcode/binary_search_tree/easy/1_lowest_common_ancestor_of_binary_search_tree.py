"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
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


def print_tree(head):
    if not head:
        return
    print(head.val)
    print_tree(head.left)
    print_tree(head.right)


class RecursiveSolution:
    """Recursive Solution.

    O(n) time complexity
    O(n) space complexity for worst case (unbalanced tree)
    O(logn) space complexity for average case (balanced tree)
    """

    def lowest_common_ancestor(self, root, p, q):
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowest_common_ancestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowest_common_ancestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root


class IterativeSolution:
    """Iterative Solution.

    O(n) time complexity
    O(1) space complexity
    """

    def lowest_common_ancestor(self, root, p, q):
        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node


if __name__ == "__main__":
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 8
    root = list_to_binary_tree(root)
    instance = RecursiveSolution()
    print_tree(instance.lowest_common_ancestor(root, p, q))
