# https://leetcode-cn.com/problems/non-overlapping-intervals/
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        intervals = sorted(intervals, key=lambda x:x[1])

        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                end = intervals[i][1]
                count += 1

        return len(intervals) - count