# https://leetcode.com/problems/clone-graph/
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.__cloned_nodes = dict()

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        existing = self.__cloned_nodes.get(node.val)
        if existing:
            return existing

        clone = Node(node.val)
        self.__cloned_nodes[node.val] = clone

        cloned_neighbors = []
        for orig_neighbor in node.neighbors:
            cloned_neighbor = self.__cloned_nodes.get(orig_neighbor.val, self.cloneGraph(orig_neighbor))
            cloned_neighbors.append(cloned_neighbor)
        clone.neighbors = cloned_neighbors

        return clone
