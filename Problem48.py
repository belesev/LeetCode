# https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)

        for depth in range(math.ceil(length/2)):
            for i in range(depth, length-1-depth):
                # remember first value to temp before rotating
                tmp = matrix[depth][i]
                matrix[depth][i] = matrix[length-1-i][depth]
                matrix[length-1-i][depth] = matrix[length-1-depth][length-1-i]
                matrix[length-1-depth][length-1-i] = matrix[i][length-1-depth]
                matrix[i][length-1-depth] = tmp
