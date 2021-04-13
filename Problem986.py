# https://leetcode.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and
# secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.
#
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed
# interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
from typing import List


class Solution:
    def intervalIntersection (self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not len(firstList) or not len(secondList):
            return []

        result = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            finish = min(firstList[i][1], secondList[j][1])
            if start <= finish:
                new_interval = [start, finish]
                result.append(new_interval)

            # move that one, whose finish is earlier
            if secondList[j][1] < firstList[i][1]:
                j += 1
            else:
                i += 1

        return result
