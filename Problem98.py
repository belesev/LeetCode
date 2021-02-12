# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.__is_valid_bst(root, [], [])

    def __is_valid_bst(self, node: TreeNode, to_be_lt: List[int], to_be_gt: List[int]) -> bool:
        for lt in to_be_lt:
            if node.val >= lt:
                return False
        for gt in to_be_gt:
            if node.val <= gt:
                return False

        to_be_lt.append(node.val)
        if node.left and not self.__is_valid_bst(node.left, to_be_lt, to_be_gt):
            return False
        to_be_lt.pop()

        to_be_gt.append(node.val)
        if node.right and not self.__is_valid_bst(node.right, to_be_lt, to_be_gt):
            return False
        to_be_gt.pop()

        return True
