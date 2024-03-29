"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

https://leetcode.com/problems/merge-two-sorted-lists/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class IterationSolution:
    """Iteration Solution.

    O(n + m) time complexity
    O(1) space complexity
    """

    def merge_two_lists(self, list_1, list_2):
        prehead = ListNode(-1)

        prev = prehead
        while list_1 and list_2:
            if list_1.val <= list_2.val:
                prev.next = list_1
                list_1 = list_1.next
            else:
                prev.next = list_2
                list_2 = list_2.next
            prev = prev.next

        # At least one of list_1 and list_2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = list_1 if list_1 is not None else list_2

        return prehead.next


class RecursiveSolution:
    """Recursive Solution.

    O(n + m) time complexity
    O(n + m) space complexity
    """

    def merge_two_lists(self, list_1, list_2):
        if list_1 is None:
            return list_2
        elif list_2 is None:
            return list_1
        elif list_1.val < list_2.val:
            list_1.next = self.merge_two_lists(list_1.next, list_2)
            return list_1
        else:
            list_2.next = self.merge_two_lists(list_1, list_2.next)
            return list_2


def list_to_linked_list(list):
    while list:
        return ListNode(list.pop(0), list_to_linked_list(list))
    return None


if __name__ == "__main__":
    nums_1 = [1, 2, 4]
    nums_2 = [1, 3, 4]
    head_1 = list_to_linked_list(nums_1)
    head_2 = list_to_linked_list(nums_2)
    instance = IterationSolution()
    new_head = instance.merge_two_lists(head_1, head_2)
    while new_head:
        print(new_head)
        new_head = new_head.next
