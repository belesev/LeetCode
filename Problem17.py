# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map
# to any letters.
from typing import List


class Solution:
    def __init__(self):
        self.__mapping = {'2': ['a', 'b', 'c'],
                          '3': ['d', 'e', 'f'],
                          '4': ['g', 'h', 'i'],
                          '5': ['j', 'k', 'l'],
                          '6': ['m', 'n', 'o'],
                          '7': ['p', 'q', 'r', 's'],
                          '8': ['t', 'u', 'v'],
                          '9': ['w', 'x', 'y', 'z']}

    def letterCombinations (self, digits: str) -> List[str]:
        result = []
        self.__comb('', digits, result)
        return result

    def __comb(self, prefix: str, digits: str, result: List[str]):
        if not(len(digits)):
            return

        digit = digits[0]
        for letter in self.__mapping[digit]:
            if len(digits) == 1:
                res = prefix + letter
                result.append(res)
            else:
                self.__comb(prefix + letter, digits[1:], result)
