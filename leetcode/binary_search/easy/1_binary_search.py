"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/binary-search/
"""


class BinarySearchSolution:
    """Binary Search Solution.

    O(logn) time complexity
    O(1) space complexity
    """

    def search(self, nums, target):
        left_index = 0
        right_index = len(nums) - 1
        while left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2
            if nums[middle_index] == target:
                return middle_index

            if nums[middle_index] > target:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    instance = BinarySearchSolution()
    print(instance.search(nums, target))
