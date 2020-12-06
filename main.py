from Problem3 import Solution as Solution3
from Problem24 import Solution as Solution24
from Problem33 import Solution as Solution33
from Problem93 import Solution as Solution93
from Problem11 import Solution as Solution11
from Problem387 import Solution as Solution387
from Problem21 import Solution as Solution21
from Problem21 import ListNode
from Problem169 import Solution as Solution169
from Problem121 import Solution as Solution121

def __problem3():
    solution = Solution3()
    result = solution.lengthOfLongestSubstring("abcxxabcdee")
    print()
    print("Result is", result)

def __problem24():
    solution = Solution24()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    #node = ListNode(1, None)
    #node = ListNode(1, ListNode(2, None))
    #node = None
    result = solution.swapPairs(node)
    while result:
        print(result.val, " -> ")
        result = result.next

def __problem33():
    solution = Solution33()
    #result = solution.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 0)
    #result = solution.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 7)
    #result = solution.search([4, 5, 6, 7, 8, 0, 1, 2], 3)
    #result = solution.search([4, 5, 6, 7, 0, 1, 2, 3], 0)
    result = solution.search([4, 5, 6, 0, 1, 2, 3], 6)
    #result = solution.search([4, 5, 0, 1, 2, 3], 0)
    #result = solution.search([4, 0, 1, 2, 3], 0)
    #result = solution.search([4, 0, 1, 2], 0)
    #result = solution.search([4, 0, 1], 0)
    #result = solution.search([4, 0], 0)
    #result = solution.search([0], 0)
    #result = solution.search([4], 0)
    #result = solution.search([1, 3], 1)
    #result = solution.search([1, 3], 0)
    print("Target is at", result, "position")

def __problem93():
    solution = Solution93()
    result = solution.restoreIpAddresses("101023")
    for ip in result:
        print(ip)

def __problem11():
    solution = Solution11()
    result = solution.maxArea([8,2,6,2,10,2,5,9])
    print(result)

def __problem387():
    solution = Solution387()
    result = solution.firstUniqChar("leecodevl")
    print(result)

def __problem21():
    solution = Solution21()
    result = solution.mergeTwoLists(ListNode(0, ListNode(2, None)), ListNode(0, ListNode(2, ListNode(3, ListNode(6, None)))))
    while result:
        print(result.val, " -> ")
        result = result.next

def __problem169():
    solution = Solution169()
    result = solution.majorityElement([1,2,3,4,1,2,2,2,2])
    print(result)

def __problem121():
    solution = Solution121()
    result = solution.maxProfit([2,1,2,4,1,2])
    print(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    __problem121()
