"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

https://leetcode.com/problems/maximum-subarray/
"""


class BruteForceSolution:
    """Brute force solution.

    O(n^2) time complexity
    O(1) space complexity
    """

    def max_sub_array(self, nums):
        length = len(nums)
        max_sum = max(nums)
        for i in range(length):
            sum = nums[i]
            for j in range(i + 1, length):
                sum += nums[j]
                max_sum = max(max_sum, sum)
        return max_sum


class DynamicSolution:
    """Dynamic Programming Solution.


    O(n) time complexity
    O(1) space complexity
    """

    def max_sub_array(self, nums):
        length = len(nums)
        max_sum = nums[0]
        current_sum = 0
        for i in range(length):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    nums = [5, 4, -1, 7, 8]
    obj = DynamicSolution()
    print(obj.max_sub_array(nums))
