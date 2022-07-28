"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

https://leetcode.com/problems/permutations/
"""


class BackTrackSolution:
    """Back Track Solution.

    O(∑P(n, k)) time complexity where P(n, k) is k-permuations of n (better than
    O(n * n!) but worse than O(n!)) https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n
    O(n!) space complexity
    """

    def permute(self, nums):
        permutations = []
        n = len(nums)

        def backtrack(index=0):
            if index == n:
                permutations.append(nums[:])
            for i in range(index, n):
                # place i-th integer first
                # in the current permutation
                nums[index], nums[i] = nums[i], nums[index]
                # use next integers to complete the permutations
                backtrack(index + 1)
                # backtrack
                nums[index], nums[i] = nums[i], nums[index]

        backtrack()

        return permutations


if __name__ == "__main__":
    nums = [1, 2, 3]
    instance = BackTrackSolution()
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(instance.permute(nums))
