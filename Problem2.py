# https://leetcode.com/problems/add-two-numbers/submissions/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_head = ListNode()

        previous = result_head
        carry = 0

        # move on while any of the lists has not ended or there's a carry (last digit)
        while l1 or l2 or carry != 0:
            new_value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            current = ListNode(new_value % 10)
            previous.next = current
            carry = new_value // 10
            previous = current

            # move on along lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result_head.next
