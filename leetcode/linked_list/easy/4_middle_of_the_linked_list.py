"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

https://leetcode.com/problems/middle-of-the-linked-list/
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

    def middle_node(self, head):
        count = 0
        current_node = head
        while current_node:
            count += 1
            current_node = current_node.next
        count = 6
        middle = count // 2
        for _ in range(middle):
            head = head.next
        return head


class OutputToArraySolution:
    """Output to array.

    O(n) time complexity
    O(n) space complexity
    """

    def middle_node(self, head):
        array = []
        while head:
            array.append(head)
            head = head.next
        return array[len(array) // 2]


class FastAndSlowPointerSolution:
    """Fast and slow pointer solution.

    O(n) time complexity
    O(1) space complexity
    """

    def middle_node(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def list_to_linked_list(list):
    while list:
        return ListNode(list.pop(0), list_to_linked_list(list))
    return None


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    head = list_to_linked_list(nums)
    instance = IterativeSolution()
    new_head = instance.middle_node(head)
    while new_head:
        print(new_head)
        new_head = new_head.next
