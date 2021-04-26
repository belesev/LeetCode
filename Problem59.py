# https://leetcode.com/problems/spiral-matrix-ii/
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Example: Input: n = 3   # Output: [[1,2,3],[8,9,4],[7,6,5]]
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cnt = 0
        matrix = [[0] * n for i in range(n)]
        i = 0
        j = 0
        shift_i = 1
        shift_j = 0
        while cnt < n * n:
            # turn down / up
            if shift_i != 0 and (i + shift_i == n or i + shift_i < 0 or matrix[j][i+shift_i] != 0):
                shift_j = 1 if shift_i > 0 else -1
                shift_i = 0
            # turn left / right
            elif shift_j != 0 and (j + shift_j == n or j + shift_j < 0 or matrix[j+shift_j][i] != 0):
                shift_i = 1 if shift_j < 0 else -1
                shift_j = 0

            matrix[j][i] = cnt+1
            cnt += 1
            i += shift_i
            j += shift_j

        return matrix
