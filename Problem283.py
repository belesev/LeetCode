# https://leetcode.com/problems/move-zeroes/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or not len(nums):
            return

        count_zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zeros += 1
                continue
            else:
                nums[i-count_zeros] = nums[i]

        for i in range(len(nums) - count_zeros, len(nums)):
            nums[i] = 0
