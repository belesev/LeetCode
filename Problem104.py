# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.__max_depth(root, 1, 0)

    def __max_depth(self, node: TreeNode, depth, max_depth) -> int:
        if not node:
            # return max_depth with no change
            return max_depth
        # for leaf nodes return maximum (current depth, maximum known depth)
        if not node.left and not node.right:
            return max(depth, max_depth)

        # for parent nodes return maximum (left, right) branches
        left = self.__max_depth(node.left, depth + 1, max_depth)
        right = self.__max_depth(node.right, depth + 1, max_depth)
        return max(left, right)
