# https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        entrances = dict()
        for p in nums:
            new_value = entrances.get(p, 0) + 1
            if new_value > len(nums)/2:
                return p
            entrances[p] = new_value
