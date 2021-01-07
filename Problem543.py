# https://leetcode.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is
# the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth_tree_root = self.__build_depth_tree(root)
        return self.__find_max_children_sum(depth_tree_root)

    def __find_max_children_sum(self, node: TreeNode):
        if not node.left and not node.right:
            return 0
        elif node.left and not node.right:
            return node.left.val + 1
        elif node.right and not node.left:
            return node.right.val + 1
        else:
            own_value = node.left.val + node.right.val + 2
            return max(self.__find_max_children_sum(node.left),
                       self.__find_max_children_sum(node.right),
                       own_value)

    def __build_depth_tree(self, node: TreeNode):
        if not node.left and not node.right:
            return TreeNode(0)
        left_sub = self.__build_depth_tree(node.left) if node.left else None
        right_sub = self.__build_depth_tree(node.right) if node.right else None
        value = max(left_sub.val if left_sub else 0, right_sub.val if right_sub else 0) + 1
        return TreeNode(value, left_sub, right_sub)