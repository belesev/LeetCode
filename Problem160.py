# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None

        # 1. count length of both
        tmpHeadA = headA
        lenA = 0
        while tmpHeadA:
            tmpHeadA = tmpHeadA.next
            lenA += 1

        tmpHeadB = headB
        lenB = 0
        while tmpHeadB:
            tmpHeadB = tmpHeadB.next
            lenB += 1

        # 2. align length of both
        # count minimum length
        # and skip first diffCount items in the bigger List
        len = min(lenA, lenB)

        if lenA - len > 0:
            for i in range(lenA - len):
                headA = headA.next
        elif lenB - len > 0:
            for i in range(lenB - len):
                headB = headB.next

        # 3. step synchronously in both lists
        # and check every step if this is the same node in both lists

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
