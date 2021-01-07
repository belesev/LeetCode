# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = set()
        for i in range(1, len(nums)+1):
            result.add(i)
        for num in nums:
            if num not in result:
                continue
            result.remove(num)
        return list(result)
