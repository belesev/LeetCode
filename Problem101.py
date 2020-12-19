# https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        # left-root-right push to stack from left branch, then continue,
        # popping from stack and comparing from right branch
        stack_left = []
        stack_right = []
        self.append_stack_left_to_right(stack_left, root.left, 1)
        self.append_stack_right_to_left(stack_right, root.right, 1)
        while len(stack_left) and len(stack_right):
            (item_left, level_left) = stack_left.pop(0)
            (item_right, level_right) = stack_right.pop(0)
            if item_left != item_right:
                return False
            if level_left != level_right:
                return False
        return len(stack_left) == 0 and len(stack_right) == 0

    def append_stack_left_to_right(self, stack: [], node: TreeNode, level: int):
        if not node:
            stack.append((None, level))
            return
        # if node has at least one child, then append both
        # even if one of them is None
        if node.left or node.right:
            self.append_stack_left_to_right(stack, node.left, level+1)
        stack.append((node.val, level))
        if node.left or node.right:
            self.append_stack_left_to_right(stack, node.right, level+1)

    def append_stack_right_to_left(self, stack: [], node: TreeNode, level: int):
        if not node:
            stack.append((None, level))
            return
        if node.left or node.right:
            self.append_stack_right_to_left(stack, node.right, level+1)
        stack.append((node.val, level))
        if node.left or node.right:
            self.append_stack_right_to_left(stack, node.left, level+1)