# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
class Solution:
    def __is_pair(self, opening, closing):
        if opening == '(' and closing == ')':
            return True
        if opening == '{' and closing == '}':
            return True
        if opening == '[' and closing == ']':
            return True
        return False

    def isValid(self, s: str) -> bool:
        stack = []
        opening_symbols = ['(', '{', '[']

        for ch in s:
            if ch in opening_symbols:
                # for opening symbol push to the stack
                stack.append(ch)
            else:
                # for closing symbol check that there's something in the stack to pop
                if not len(stack):
                    return False
                # for popped element compare if it's an opening pair for the current symbol
                popped = stack.pop()
                if not self.__is_pair(popped, ch):
                    return False

        # return True if stack became empty
        return not len(stack)
