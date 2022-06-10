"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

https://leetcode.com/problems/linked-list-cycle/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SetSolution:
    """Set Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def has_cycle(self, head):
        if not head:
            return False
        seen_nodes = set()
        while head:
            if head in seen_nodes:
                return True
            seen_nodes.add(head)
            head = head.next
        return False


class CycleFindingSolution:
    """Floyd's Cycle Finding Algorithm

    The space complexity can be reduced to O(1) by considering two pointers at different speed - a slow pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

    If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.

    O(n) time complexity
    O(1) space complexity
    """

    def has_cycle(self, head):
        if not head:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while slow_pointer != fast_pointer:
            if fast_pointer is None or fast_pointer.next is None:
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return True


if __name__ == "__main__":
    head = [3, 2, 0, -4]
    obj = SetSolution()
    print(obj.has_cycle(head))
