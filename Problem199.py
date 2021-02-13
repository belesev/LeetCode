# https://leetcode.com/problems/binary-tree-right-side-view/
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
# ordered from top to bottom.

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.by_depth = dict()

    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []

        # simple BSF with storing iterated nodes by depth
        self.__dsf(root, 0)

        for k, v in self.by_depth.items():
            result.append(v.pop())
        return result

    def __dsf(self, node: TreeNode, depth: int) -> None:
        if not node:
            return

        if depth not in self.by_depth:
            self.by_depth[depth] = []

        if node.left:
            self.__dsf(node.left, depth + 1)
        self.by_depth[depth].append(node.val)
        if node.right:
            self.__dsf(node.right, depth + 1)
