"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IterativeSolution:
    """Iterative Solution.

    O(n) time complexity
    O(1) space complexity
    """

    def reverse_list(self, head):
        if head.next is None:
            return head

        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node


class RecursiveSolution:
    """Recursive Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def reverse_list(self, head):
        if not head or not head.next:
            return head

        previous_node = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return previous_node


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    obj = IterativeSolution()
    print(obj.reverse_list(head))
