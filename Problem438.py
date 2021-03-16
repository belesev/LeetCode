# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than
# 20,100.
# The order of output does not matter.

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []

        if len(p) > len(s):
            return answer

        letters = dict()
        for i in range(len(p)):
            ch = s[i]
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1

        ethalon = dict()
        for j in range(len(p)):
            ch = p[j]
            if ch in ethalon:
                ethalon[ch] += 1
            else:
                ethalon[ch] = 1

        shift = 0
        while True:
            if letters == ethalon:
                answer.append(shift)

            if shift + 1 + len(p) > len(s):
                break

            ch = s[shift]
            letters[ch] -= 1
            if letters[ch] == 0:
                letters.pop(ch, None)

            shift += 1

            ch = s[shift+len(p) - 1]
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1

        return answer

