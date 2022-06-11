"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


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


def list_to_linked_list(list):
    while list:
        return ListNode(list.pop(0), list_to_linked_list(list))
    return None


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    head = list_to_linked_list(nums)
    instance = IterativeSolution()
    new_head = instance.reverse_list(head)
    while new_head:
        print(new_head)
        new_head = new_head.next
