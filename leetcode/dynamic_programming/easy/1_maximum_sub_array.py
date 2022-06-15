"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    """Solution.

    O(n) time complexity
    O(1) space complexity
    """

    def max_sub_array(self, nums):
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    instance = Solution()
    print(instance.max_sub_array(nums))
