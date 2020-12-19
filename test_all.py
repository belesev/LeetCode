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
from Problem53 import Solution as Solution53
from Problem20 import Solution as Solution20
from Problem70 import Solution as Solution70
from Problem101 import Solution as Solution101
from Problem101 import TreeNode as TreeNode
from Problem104 import Solution as Solution104
from Problem136 import Solution as Solution136
from Problem141 import Solution as Solution141


def test_problem3():
    solution = Solution3()
    result = solution.lengthOfLongestSubstring("abcxxabcdee")
    assert 6 == result


def test_problem24():
    solution = Solution24()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    result = solution.swapPairs(node)
    expected = [2, 1, 4, 3]
    while result:
        print(result.val, " -> ")
        expected_item = expected.pop(0)
        assert expected_item == result.val
        result = result.next

    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    #node = ListNode(1, None)
    #node = ListNode(1, ListNode(2, None))
    #node = None


def test_problem33():
    solution = Solution33()
    result = solution.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 0)
    assert 5 == result
    result = solution.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 7)
    assert 3 == result
    result = solution.search([4, 5, 6, 7, 8, 0, 1, 2], 3)
    assert -1 == result
    result = solution.search([4, 5, 6, 7, 0, 1, 2, 3], 0)
    assert 4 == result
    result = solution.search([4, 5, 6, 0, 1, 2, 3], 6)
    assert 2 == result
    result = solution.search([4, 5, 0, 1, 2, 3], 0)
    assert 2 == result
    result = solution.search([4, 0, 1, 2, 3], 0)
    assert 1 == result
    result = solution.search([4, 0, 1, 2], 0)
    assert 1 == result
    result = solution.search([4, 0, 1], 0)
    assert 1 == result
    result = solution.search([4, 0], 0)
    assert 1 == result
    result = solution.search([0], 0)
    assert 0 == result
    result = solution.search([4], 0)
    assert -1 == result
    result = solution.search([1, 3], 1)
    assert 0 == result
    result = solution.search([1, 3], 0)
    assert -1 == result


def test_problem93():
    solution = Solution93()
    result = solution.restoreIpAddresses("101023")
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert expected == result
    for ip in result:
        print(ip)


def test_problem11():
    solution = Solution11()
    result = solution.maxArea([8,2,6,2,10,2,5,9])
    assert 56 == result


def test_problem387():
    solution = Solution387()
    result = solution.firstUniqChar("leecodevl")
    assert 3 == result


def test_problem21():
    solution = Solution21()
    result = solution.mergeTwoLists(ListNode(0, ListNode(2, None)), ListNode(0, ListNode(2, ListNode(3, ListNode(6, None)))))
    expected = [0, 0, 2, 2, 3, 6]
    while result:
        print(result.val, " -> ")
        expected_item = expected.pop(0)
        assert expected_item == result.val
        result = result.next


def test_problem169():
    solution = Solution169()
    result = solution.majorityElement([1, 2, 3, 4, 1, 2, 2, 2, 2])
    assert 2 == result

def test_problem53():
    solution = Solution53()
    result = solution.maxSubArray([1, 0, -2, 1, -2])
    assert 1 == result
    result = solution.maxSubArray([1, 0, -2, 3, -2, 5])
    assert 6 == result


def test_problem121():
    solution = Solution121()
    result = solution.maxProfit([7, 2])
    assert 0 == result
    result = solution.maxProfit([1, 5, 4, 10])
    assert 9 == result
    result = solution.maxProfit([2, 10, 1, 11])
    assert 10 == result


def test_problem20():
    solution = Solution20()
    result = solution.isValid("{()[}]")
    assert not result
    result = solution.isValid("{()[]}")
    assert result
    result = solution.isValid("{")
    assert not result


def test_problem70():
    result = Solution70().climbStairs(5)
    assert 8 == result


def test_problem101():
    solution = Solution101()
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert solution.isSymmetric(root)
    root = TreeNode(1, TreeNode(2))
    assert not solution.isSymmetric(root)
    root = TreeNode(1)
    assert solution.isSymmetric(root)
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert not solution.isSymmetric(root)
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3), None))
    assert solution.isSymmetric(root)
    root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))
    assert not solution.isSymmetric(root)
    root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, None, TreeNode(2)))
    assert solution.isSymmetric(root)
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert not solution.isSymmetric(root)
    root = None
    assert solution.isSymmetric(root)
    # equal traversal sequence
    root = TreeNode(5, TreeNode(4, None, TreeNode(1, TreeNode(2))), TreeNode(1, None, TreeNode(4, TreeNode(2))))
    assert not solution.isSymmetric(root)


def test_problem104():
    solution = Solution104()
    result = solution.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    assert 3 == result
    result = solution.maxDepth(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(5)))))
    assert 4 == result
    result = solution.maxDepth(TreeNode(1, None, TreeNode(2)))
    assert 2 == result
    result = solution.maxDepth(None)
    assert 0 == result


def test_problem136():
    assert 1 == Solution136().singleNumber([2, 2, 1])
    assert 4 == Solution136().singleNumber([4, 1, 2, 1, 2])
    assert 1 == Solution136().singleNumber([1])


def test_problem141():
    solution = Solution141()
    pseudo_tail = ListNode(-4)
    pos = ListNode(2, ListNode(0, pseudo_tail))
    pseudo_tail.next = pos
    head = ListNode(3, pos)
    assert solution.hasCycle(head)

    assert not solution.hasCycle(ListNode(1))

    tail = ListNode(2)
    head = ListNode(1, tail)
    assert not solution.hasCycle(head)

    tail.next = head
    assert solution.hasCycle(head)
