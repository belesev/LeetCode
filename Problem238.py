# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
from typing import List


class Solution:
    def productExceptSelf (self, nums: List[int]) -> List[int]:
        product_all = 1
        count_zeros = 0
        pos_zero = 0

        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                product_all = product_all * num
            else:
                count_zeros += 1
                pos_zero = i

        result = []
        if count_zeros >= 1:
            for _ in range(len(nums)):
                result.append(0)
            if count_zeros == 1:
                result[pos_zero] = product_all
            return result

        for num in nums:
            result.append(round(product_all / num))
        return result
