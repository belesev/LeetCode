# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_elems = dict()

        for num in nums:
            count_elems[num] = count_elems.get(num, 0) + 1

        unique_elems = sorted(set(count_elems.keys()))

        cumulated = 0
        dict_less_than = dict()
        for num in unique_elems:
            dict_less_than[num] = cumulated
            cumulated += count_elems[num]

        result = []
        for num in nums:
            result.append(dict_less_than[num])

        return result
