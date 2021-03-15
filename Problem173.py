# https://leetcode.com/problems/binary-search-tree-iterator/
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the
# constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise
# returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
# smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order
# traversal when next() is called.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LinkedListTreeNode:
    def __init__(self, node: TreeNode):
        self.node = node
        self.next = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.__ptr = LinkedListTreeNode(None)
        self.__traverse(root, self.__ptr)

    def next(self) -> int:
        self.__ptr = self.__ptr.next
        return self.__ptr.node.val

    def hasNext(self) -> bool:
        if self.__ptr.next:
            return True
        return False

    def __traverse(self, node: TreeNode, previous: LinkedListTreeNode) -> LinkedListTreeNode:
        # left
        current = LinkedListTreeNode(node)

        if node.left:
            rightmost_from_left = self.__traverse(node.left, previous)
            rightmost_from_left.next = current
        else:
            previous.next = current

        # right
        rightmost = current
        if node.right:
            rightmost = self.__traverse(node.right, current)

        return rightmost
