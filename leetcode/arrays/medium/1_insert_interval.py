"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

https://leetcode.com/problems/insert-interval/
"""


class BruteForceSolution:
    """Brute force solution.

    O(nlogn) time complexity
    O(n) space complexity
    """

    def insert(self, intervals, new_interval):
        n = len(intervals)
        i = 0
        new_intervals = []

        # Append first non-overlapping intervals
        while i < n and intervals[i][1] < new_interval[0]:
            new_intervals.append(intervals[i])
            i += 1

        # Merge overlapping intervals (if no overlapping then just append new_interval)
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            i += 1
        new_intervals.append(new_interval)

        # Append remaining non-overlapping intervals
        while i < n:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    obj = BruteForceSolution()
    print(obj.insert(intervals, new_interval))
    # [[1,5],[6,9]]
