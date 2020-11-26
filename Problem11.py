from typing import List, OrderedDict


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = min(height[0], height[-1]) * (len(height) - 1)
        left = 0
        right = len(height) - 1

        while left < right:
            candidate = min(height[left+1], height[right]) * (right - left - 1)
            if candidate > result:
                result = candidate
                left += 1
                continue

            candidate = min(height[left], height[right-1]) * (right - left - 1)
            if candidate > result:
                result = candidate
                right -= 1
                continue

            left += 1
            right -= 1

        return result