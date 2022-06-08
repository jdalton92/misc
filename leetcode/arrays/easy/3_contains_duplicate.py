"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

https://leetcode.com/problems/contains-duplicate/
"""


class SortingSolution:
    """Sorting solution.

    * O(n) time complexity
    * O(1) space complexity
    """

    def contains_duplicate(self, nums):
        nums.sort()
        length = len(nums)
        for i in range(1, length):
            if nums[i] == nums[i + 1]:
                return True

        return False


class SetSolution:
    """Set solution.

    * O(1) time complexity
    * O(1) space complexity
    """

    def contains_duplicate(self, nums):
        unique_nums = set(nums)
        return len(unique_nums) < len(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    obj = SetSolution()
    print(obj.contains_duplicate(nums))
