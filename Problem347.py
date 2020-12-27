# https://leetcode.com/problems/top-k-frequent-elements/
# Given a non-empty array of integers, return the k most frequent elements.
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        values_by_frequency = dict()

        for i in range(len(nums)):
            # count frequency for each element
            x = nums[i]
            old_value = frequency.get(x) if x in frequency else 0
            new_value = old_value + 1
            frequency[x] = new_value

            # reversed mapping: dictionary <frequency, set of numbers>
            # add current number 'x' to the new frequency record
            if new_value not in values_by_frequency:
                values_by_frequency[new_value] = set()

            vals = values_by_frequency[new_value]
            vals.add(x)

            # remove current number 'x' from the previous frequency record
            if old_value in values_by_frequency:
                values_by_frequency[old_value].remove(x)

        answer = list()
        i = 0
        # keys sorted descending
        result_frequency_desc = sorted(values_by_frequency, reverse=True)
        while i < k:
            # pop another one key and extend values from this key to the result
            # until it becomes 'k' pieces
            vals = values_by_frequency[result_frequency_desc.pop(0)]
            answer.extend(vals)
            i += len(vals)

        return answer
