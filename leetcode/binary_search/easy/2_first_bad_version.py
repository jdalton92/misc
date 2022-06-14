"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

https://leetcode.com/problems/first-bad-version/
"""


class BinarySearchSolution:
    """Binary Search Solution.

    O(logn) time complexity
    O(1) space complexity
    """

    def first_bad_version(self, n):
        left_index = 1
        right_index = n
        while left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2
            if isBadVersion(middle_index):
                right_index = middle_index
            else:
                left_index = middle_index + 1
        return left_index


if __name__ == "__main__":
    n = 5
    instance = BinarySearchSolution()
    print(instance.search(n))
