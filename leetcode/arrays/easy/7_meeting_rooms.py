"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

https://leetcode.com/problems/meeting-rooms/
"""


class Solution:
    """Solution.

    O(nlogn) time complexity (nlogn due to sorting)
    O(1) space complexity
    """

    def can_attend_meeting(self, intervals):
        intervals.sort(key=lambda x: x[0])
        count = len(intervals)
        i = 0
        for i in range(count - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


if __name__ == "__main__":
    # intervals = [[0, 30], [5, 10], [15, 20]]
    intervals = [[13, 15], [1, 13]]
    instance = Solution()
    print(instance.can_attend_meeting(intervals))
