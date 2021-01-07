# https://leetcode.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        node = head
        count = 0
        while node:
            count += 1
            node = node.next

        if count == 1:
            return True

        half_count = count // 2

        # skip half of list
        node = head
        prev = None
        for i in range(half_count):
            prev = node
            node = node.next

        # break the first half of the list
        prev.next = None

        if count % 2 == 1:
            if not node:
                return False
            node = node.next

        # start of the second part of the list
        second_head = node

        # reverse second part of the list
        second_head = self.__reverse(second_head)

        # move along head and second_head and compare pairs
        while head and second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next

        # return True if both lists ran dry
        return not head and not second_head

    def __reverse(self, head: ListNode):
        if not head:
            return None

        prev = None
        while head:
            move_on = head.next
            head.next = prev
            prev = head
            head = move_on
        return prev
