# https://leetcode.com/problems/k-closest-points-to-origin/

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the
# k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(x*x + y*y)
            distances.append(distance)

        sorted_dist = sorted(distances)
        threshold = sorted_dist[K-1]

        result = list()
        i = 0
        for point in points:
            if distances[i] <= threshold:
                result.append(point)
            i += 1

        return result
