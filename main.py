# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Problem3 import Solution
from Problem24 import Solution as Solution24
from Problem24 import ListNode

def __problem3():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("abcxxabcdee")
    print()
    print("Result is", result)

def __problem24():
    sol = Solution24()
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    #node = ListNode(1, None)
    #node = ListNode(1, ListNode(2, None))
    node = None
    result = sol.swapPairs(node)
    while result:
        print(result.val, " -> ")
        result = result.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    __problem24()
