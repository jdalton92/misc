"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/
"""


class BruteForceSolution:
    """Brute force solution.

    * O(n^2) time complexity
    * O(1) space complexity
    """

    def two_sum(self, nums, target):
        length = len(nums)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


class TwoPointersSolution:
    """Two pointers solution.

    O(n) time complexity
    O(1) space complexity
    """

    def two_sum(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1

        return [left, right]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    obj = TwoPointersSolution()
    print(obj.two_sum(nums, target))
