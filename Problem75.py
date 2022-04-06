"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
from typing import List


class Solution:
    def sortColors (self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        amount_red = 0
        amount_white = 0
        amount_blue = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                amount_red += 1
            elif nums[i] == 1:
                amount_white += 1
            else:
                amount_blue += 1

        for i in range(0, amount_red):
            nums[i] = 0

        for i in range(amount_red, amount_red + amount_white):
            nums[i] = 1

        for i in range(len(nums) - amount_blue, len(nums)):
            nums[i] = 2

        return nums
