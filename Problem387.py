# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqs = dict()
        index = 0

        while index < len(s):
            c = s[index]
            if c in uniqs:
                uniqs[c] = -1
            else:
                uniqs[c] = index
            index += 1

        for key, value in uniqs.items():
            if value > -1:
                return value

        return -1