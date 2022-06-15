"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

https://leetcode.com/problems/climbing-stairs/
"""


class BruteForceSolution:
    """Brute Force Solution.

    O(2^n) time complexity
    O(n) space complexity
    """

    def climb(self, current_step, destination_step):
        if current_step > destination_step:
            return 0
        if current_step == destination_step:
            return 1

        return self.climb(current_step + 1, destination_step) + self.climb(
            current_step + 2, destination_step
        )

    def climb_stairs(self, n):
        return self.climb(0, n)


class DynamicProgrammingSolution:
    """Dynamic Programming Solution.

    The sum of the total number of ways to reach ith is equal to sum of ways of reaching
    (i-1)th and ways of reaching (i-2)th step. Eg. for 6 steps:

    [0, 1, 2, 3, 5, 8, 13]

    O(n) time complexity
    O(n) space complexity
    """

    def climb_stairs(self, n):
        if n == 1:
            return 1
        cumulative_steps = [0 for _ in range(n + 1)]
        cumulative_steps[1] = 1
        cumulative_steps[2] = 2
        for i in range(3, n + 1):
            cumulative_steps[i] = cumulative_steps[i - 1] + cumulative_steps[i - 2]
        return cumulative_steps[n]


if __name__ == "__main__":
    n = 4
    instance = DynamicProgrammingSolution()
    print(instance.climb_stairs(n))
