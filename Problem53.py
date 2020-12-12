# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which
# has the largest sum and return its sum.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # special case
        if len(nums) == 1:
            return nums[0]

        # sum_arr contains sum of all previous elements, including current
        sum_arr = []
        for i in range(len(nums)):
            sum_arr.append((sum_arr[i-1] if i > 0 else 0) + nums[i])

        # minimum possible value in sum array: if take no elements, sum is 0
        min_elem_in_sum_arr = 0

        best = sum_arr[0]
        for i in range(len(sum_arr)):
            # update best result if possible: sum at current point minus minimum possible sum
            best = max(best, sum_arr[i] - min_elem_in_sum_arr)

            # look for minimum value in sum_arr; starting subarray from this point is most profitable
            min_elem_in_sum_arr = min(min_elem_in_sum_arr, sum_arr[i])

        return best
