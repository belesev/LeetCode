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
from Problem155 import MinStack
from Problem160 import Solution as Solution160
from Problem226 import Solution as Solution226
from Problem283 import Solution as Solution283


def test_problem3():
    solution = Solution3()
    result = solution.lengthOfLongestSubstring("abcxxabcdee")
    assert result == 6


def test_problem24():
    solution = Solution24()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    result = solution.swapPairs(node)
    expected = [2, 1, 4, 3]
    while result:
        print(result.val, " -> ")
        expected_item = expected.pop(0)
        assert result.val == expected_item
        result = result.next

    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    #node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    #node = ListNode(1, None)
    #node = ListNode(1, ListNode(2, None))
    #node = None


def test_problem33():
    solution = Solution33()
    result = solution.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 0)
    assert result == 5
    result = solution.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 7)
    assert result == 3
    result = solution.search([4, 5, 6, 7, 8, 0, 1, 2], 3)
    assert result == -1
    result = solution.search([4, 5, 6, 7, 0, 1, 2, 3], 0)
    assert result == 4
    result = solution.search([4, 5, 6, 0, 1, 2, 3], 6)
    assert result == 2
    result = solution.search([4, 5, 0, 1, 2, 3], 0)
    assert result == 2
    result = solution.search([4, 0, 1, 2, 3], 0)
    assert result == 1
    result = solution.search([4, 0, 1, 2], 0)
    assert result == 1
    result = solution.search([4, 0, 1], 0)
    assert result == 1
    result = solution.search([4, 0], 0)
    assert result == 1
    result = solution.search([0], 0)
    assert result == 0
    result = solution.search([4], 0)
    assert result == -1
    result = solution.search([1, 3], 1)
    assert result == 0
    result = solution.search([1, 3], 0)
    assert result == -1


def test_problem93():
    solution = Solution93()
    result = solution.restoreIpAddresses("101023")
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert result == expected
    for ip in result:
        print(ip)


def test_problem11():
    solution = Solution11()
    result = solution.maxArea([8,2,6,2,10,2,5,9])
    assert result == 56


def test_problem387():
    solution = Solution387()
    result = solution.firstUniqChar("leecodevl")
    assert result == 3


def test_problem21():
    solution = Solution21()
    result = solution.mergeTwoLists(ListNode(0, ListNode(2, None)), ListNode(0, ListNode(2, ListNode(3, ListNode(6, None)))))
    expected = [0, 0, 2, 2, 3, 6]
    while result:
        print(result.val, " -> ")
        expected_item = expected.pop(0)
        assert result.val == expected_item
        result = result.next


def test_problem169():
    solution = Solution169()
    result = solution.majorityElement([1, 2, 3, 4, 1, 2, 2, 2, 2])
    assert result == 2

def test_problem53():
    solution = Solution53()
    result = solution.maxSubArray([1, 0, -2, 1, -2])
    assert result == 1
    result = solution.maxSubArray([1, 0, -2, 3, -2, 5])
    assert result == 6


def test_problem121():
    solution = Solution121()
    result = solution.maxProfit([7, 2])
    assert result == 0
    result = solution.maxProfit([1, 5, 4, 10])
    assert result == 9
    result = solution.maxProfit([2, 10, 1, 11])
    assert result == 10


def test_problem20():
    solution = Solution20()
    result = solution.isValid("{()[}]")
    assert not result
    result = solution.isValid("{()[]}")
    assert result == solution.isValid("{")
    assert not result


def test_problem70():
    result = Solution70().climbStairs(5)
    assert result == 8


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
    assert result == 3
    result = solution.maxDepth(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(5)))))
    assert result == 4
    result = solution.maxDepth(TreeNode(1, None, TreeNode(2)))
    assert result == 2
    result = solution.maxDepth(None)
    assert result == 0


def test_problem136():
    assert Solution136().singleNumber([2, 2, 1]) == 1
    assert Solution136().singleNumber([4, 1, 2, 1, 2]) == 4
    assert Solution136().singleNumber([1]) == 1


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


def test_problem155():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    top = min_stack.top()
    assert top == -3
    min_value = min_stack.getMin()
    assert min_value == -3

    min_stack.pop()
    top = min_stack.top()
    assert top == 0
    min_value = min_stack.getMin()
    assert min_value == -2

    min_stack.pop()
    top = min_stack.top()
    assert top == -2
    min_value = min_stack.getMin()
    assert min_value == -2


    min_stack = MinStack()
    min_stack.push(-1)
    assert min_stack.top() == -1
    assert min_stack.getMin() == -1

def test_problem160():
    solution = Solution160()
    assert not solution.getIntersectionNode(None, None)

    assert not solution.getIntersectionNode(None, ListNode(1))

    assert not solution.getIntersectionNode(ListNode(1), None)

    joint_node = ListNode(10)
    result = solution.getIntersectionNode(ListNode(1, joint_node), ListNode(2, joint_node))
    assert result == joint_node

    joint_node = ListNode(10, ListNode(11))
    result = solution.getIntersectionNode(ListNode(1, joint_node), ListNode(2, joint_node))
    assert result == joint_node

    joint_node = ListNode(10)
    result = solution.getIntersectionNode(ListNode(1, ListNode(2, joint_node)), ListNode(3, joint_node))
    assert result == joint_node

    joint_node = ListNode(10, ListNode(11))
    result = solution.getIntersectionNode(ListNode(1, ListNode(2, joint_node)), ListNode(3, joint_node))
    assert result == joint_node

def test_problem226():
    solution = Solution226()
    result = solution.invertTree(None)
    assert not result

    result = solution.invertTree(TreeNode(1))
    assert result.val == 1
    assert not result.left
    assert not result.right

    result = solution.invertTree(TreeNode(1, TreeNode(2)))
    assert result.val == 1
    assert not result.left
    assert result.right.val == 2

    result = solution.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))
    assert result.val == 4
    assert result.left.val == 7
    assert result.left.left.val == 9
    assert result.left.right.val == 6
    assert result.right.val == 2
    assert result.right.left.val == 3
    assert result.right.right.val == 1

def test_problem283():
    solution = Solution283()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 0]
    solution.moveZeroes(nums)
    assert nums == [0, 0]

    nums = None
    solution.moveZeroes(nums)
    assert not nums

    nums = []
    solution.moveZeroes(nums)
    assert not len(nums)
