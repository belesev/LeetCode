# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from typing import List


class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped = dict()

        for str in strs:
            count = HashableDict()
            for c in str:
                count[c] = count.get(c, 0) + 1

            if count not in grouped:
                grouped[count] = []

            grouped[count].append(str)

        result = []
        for (_,v) in grouped.items():
            result.append(v)

        return result
