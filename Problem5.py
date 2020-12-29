# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        backwards = ""
        for i in range(len(s)-1, -1, -1):
            backwards += s[i]

        if s == backwards:
            return s

        best_length = 0
        best = set()

        # matrix of the longest common substring length
        # calculated via dynamic programming
        L = [[0 for x in range(len(s))] for y in range(len(s))]

        for i in range(len(s)):
            for j in range(len(backwards)):
                if s[i] == backwards[j]:
                    if i == 0 or j == 0:
                        L[i][j] = 1
                    else:
                        L[i][j] = L[i-1][j-1] + 1

                    if i + j > len(s) and i + j < 2 * (len(s) - 1):
                        if L[i][j] > best_length:
                            best_length = L[i][j]
                            best_string = s[i+1-best_length:i+1]
                            best = [best_string]
                        elif L[i][j] == best_length:
                            best_string = s[i + 1 - best_length:i + 1]
                            best.append(best_string)
                else:
                    L[i][j] = 0

        return best.pop()
