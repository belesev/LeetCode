# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together
# the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = start = ListNode()
        while l1 or l2:
            if l1 and l2 and l1.val < l2.val:
                tmp = l1
                l1 = l1.next
            elif l1 and l2 and l1.val >= l2.val:
                tmp = l2
                l2 = l2.next
            elif l1:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next

            result.next = tmp
            result = result.next

        return start.next
