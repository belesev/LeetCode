# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        from_beginning = count - n
        node = head

        # removing first symbol - is a special case
        if from_beginning == 0:
            return node.next

        # step to the node previous to must-be-skipped
        for i in range(from_beginning-1):
            node = node.next
        to_skip = node.next
        node.next = to_skip.next

        return head
