"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

https://leetcode.com/problems/product-of-array-except-self/
"""


class BruteForceSolution:
    """Brute force solution.

    O(n^2) time complexity
    O(n) space complexity
    """

    def product_except_self(self, nums):
        length = len(nums)
        ans = []
        for i in range(length):
            product = 1
            for j in range(length):
                if i != j:
                    product = product * nums[j]
            ans.append(product)
        return ans


class Solution:
    """Efficient solution.

    O(n) time complexity
    O(1) space complexity
    """

    def product_except_self(self, nums):
        length = len(nums)
        ans = [1 for _ in range(length)]

        # Each item multiply by items to it's LHS
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Each item multiply by it's to it's RHS
        product = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]
        return ans


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    obj = Solution()
    print(obj.product_except_self(nums))
