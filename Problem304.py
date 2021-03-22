# https://leetcode.com/problems/range-sum-query-2d-immutable/
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
#
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the elements of the matrix array inside the
# rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
from typing import List


class NumMatrix:

    def __init__ (self, matrix: List[List[int]]):
        sub_sum = []
        for i in range(len(matrix)):
            new = []
            for j in range(len(matrix[i])):
                new.append((new[j-1] if j > 0 else 0) +
                           (sub_sum[i - 1][j] if i > 0 else 0) -
                           (sub_sum[i - 1][j - 1] if j > 0 and i > 0 else 0) +
                           matrix[i][j])
            sub_sum.append(new)
        self.__sub_sum = sub_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.__sub_sum[row2][col2] - \
               (self.__sub_sum[row2][col1-1] if col1 > 0 else 0) - \
               (self.__sub_sum[row1-1][col2] if row1 > 0 else 0) + \
               (self.__sub_sum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)