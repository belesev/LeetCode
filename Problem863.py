# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# We are given a binary tree (with root node root), a target node, and an integer value K.
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned
# in any order.


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def distanceK (self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parents = dict()
        self.dfs(root, None, parents)

        visited = set()
        visited.add(target.val)
        result = []
        self.search_at_distance(target, K, result, parents, visited)

        return result

    def dfs(self, node: TreeNode, parent: TreeNode, parents: dict):
        if not node:
            return
        parents[node.val] = parent
        self.dfs(node.left, node, parents)
        self.dfs(node.right, node, parents)

    def search_at_distance(self, node: TreeNode, k: int, result: list, parents: dict, visited: set):
        if not node:
            return

        visited.add(node.val)

        if k == 0:
            result.append(node.val)
            return

        if node.left and node.left.val not in visited:
            self.search_at_distance(node.left, k-1, result, parents, visited)

        if node.right and node.right.val not in visited:
            self.search_at_distance(node.right, k-1, result, parents, visited)

        parent = parents[node.val]
        if parent and parent.val not in visited:
            self.search_at_distance(parent, k-1, result, parents, visited)
