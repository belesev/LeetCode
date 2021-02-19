# https://leetcode.com/problems/merge-intervals/
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
# of the non-overlapping intervals that cover all the intervals in the input.
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        tmp = []
        for interval in intervals:
            # if new elem overlaps the stack top
            if len(tmp) and tmp[-1][0] <= interval[0] <= tmp[-1][1]:
                # and new ending > stack top's ending, then update stack top's ending
                if interval[1] > tmp[-1][1]:
                    tmp[-1][1] = interval[1]
            else:
                tmp.append(interval)

        return tmp