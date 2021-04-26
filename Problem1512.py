# https://leetcode.com/problems/number-of-good-pairs/
# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = dict()
        result = 0
        for num in nums:
            already_met_times = count.get(num, 0)
            result += already_met_times
            count[num] = already_met_times + 1
        return result
