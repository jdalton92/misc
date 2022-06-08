"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

https://leetcode.com/problems/majority-element/
"""


class BruteForceSolution:
    """Brute force solution.

    O(n^2) time complexity
    O(1) space complexity
    """

    def majority_count(self, nums):
        min_count = len(nums) // 2
        for num in nums:
            count = sum(1 for n in nums if n == num)
            if count > min_count:
                return num


class HashMapSolution:
    """Hash map solution.

    O(n) time complexity
    O(1) space complexity
    """

    def majority_element(self, nums):
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
            if hash[num] > len(nums) // 2:
                return num


class SortingSolution:
    """Sorting solution.

    O(nLogn) time complexity
    O(1) space complexity
    """

    def majority_element(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    obj = HashMapSolution()
    print(obj.majority_element(nums))
