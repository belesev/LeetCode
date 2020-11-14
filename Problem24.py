# https://leetcode.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes. Only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = head
        saved_head = head
        i = 0

        current_tail = None

        while node and node.next:
            # remember link to the next pair
            tmp = node.next.next
            # set link from the previous pair to the current
            if current_tail:
                current_tail.next = node.next
            # revert link in the current pair
            node.next.next = node
            # remember the HEAD for the first iteration to return it in the end
            if not i:
                saved_head = node.next
            # restore link to the next pair
            node.next = tmp
            # remember new tail to create link from it later to the swiped element
            current_tail = node
            # move on to next iteration
            node = tmp

            i += 1

        return saved_head
