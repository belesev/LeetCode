# https://leetcode.com/problems/reverse-linked-list/
# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            # remember where to jump further
            next = node.next

            # current links to previous
            node.next = prev

            # update previous
            prev = node
            # and move on
            node = next

        return prev
