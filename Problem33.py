# https://leetcode.com/problems/search-in-rotated-sorted-array/
# You are given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.
import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # single element and it's ours
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        pivot_point = self.get_pivot_point(nums)
        if pivot_point == -1:
            return self.search_binary(nums, 0, len(nums)-1, target)

        result = -1
        if nums[0] <= target <= nums[pivot_point]:
            result = self.search_binary(nums, 0, pivot_point, target)
        if result == -1 and nums[pivot_point+1] <= target <= nums[-1]:
            result = self.search_binary(nums, pivot_point+1, len(nums)-1, target)
        return result

    @staticmethod
    def get_pivot_point(nums: List[int]):
        i = 0
        pivot_point = -1

        # looking for pivot_point, the last increasing element before drop down
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                pivot_point = i
                break
            i += 1
        return pivot_point

    def search_binary(self, nums: List[int], left_ptr: int, right_ptr: int, target: int) -> int:
        # exactly 1 element, checking it
        if left_ptr == right_ptr:
            if target == nums[left_ptr]:
                return left_ptr
            return -1

        # more than 1 element in sub-array
        middle_point = math.floor((left_ptr + right_ptr) / 2)

        if target <= nums[middle_point]:
            return self.search_binary(nums, left_ptr, middle_point, target)
        return self.search_binary(nums, middle_point+1, right_ptr, target)
