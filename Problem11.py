from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                candidate = min(height[i], height[j]) * (j-i)
                if candidate > best:
                    best = candidate
        return best
