# https://leetcode.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending
# order).
# The replacement must be in place and use only constant extra memory.
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        i = len(nums)-1
        # look for pivot
        # find rightmost elem so that nums[i-1] < nums[i]
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        i -= 1

        if i == -1:
            nums.reverse()
            return

        # look for min element in the suffix (right part)
        # as suffix is descending ordered, it means to find the rightmost element which is greater than nums[i]
        j = len(nums)-1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # swap pivot and min element from suffix
        nums[i], nums[j] = nums[j], nums[i]

        # sort the suffix ascending
        # as it's already non-increasing (check number 1 above), we may just reverse it
        i += 1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
