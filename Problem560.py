# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose
# sum equals to k
from typing import List


class Solution:
    def subarraySum (self, nums: List[int], k: int) -> int:
        sums = []
        for i in range(0, len(nums)):
            sums.append((sums[i-1] if i > 0 else 0) + nums[i])

        result = 0
        for end in range(0, len(sums)):
            for start in range(0, end):
                interval_sum = sums[end] - sums[start]
                if interval_sum == k:
                    result += 1

        return result
