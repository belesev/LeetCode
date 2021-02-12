# https://leetcode.com/problems/valid-palindrome/
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
import math


class Solution:
    def isPalindrome(self, s: str) -> bool:
        purified = ''
        for c in s:
            if ord("0") <= ord(c) <= ord("9") or ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z"):
                purified += c

        st = []
        for c in range(math.floor(len(purified) / 2)):
            st.append(purified[c])

        for c in range(math.ceil(len(purified) / 2), len(purified)):
            if st.pop().lower() != purified[c].lower():
                return False

        return True
