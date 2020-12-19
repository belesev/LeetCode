# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for p in nums:
            result = result ^ p
        return result
