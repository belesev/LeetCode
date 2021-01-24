# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count_nums = self.__prepare_dict(nums)
        result = set()

        for first_index in range(len(nums)):
            first = nums[first_index]
            for second_index in range(first_index+1, len(nums)):
                second = nums[second_index]

                missing_third = 0 - first - second
                if missing_third not in count_nums:
                    continue
                count_third = count_nums[missing_third]
                if missing_third == first:
                    count_third -= 1
                if missing_third == second:
                    count_third -= 1
                if count_third > 0:
                    ordered_tuple = sorted((first, second, missing_third))
                    result.add(tuple(ordered_tuple))
        return result

    def __prepare_dict(self, nums: List[int]):
        result = dict()
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        return result
