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
from Problem347 import Solution as Solution347
from Problem5 import Solution as Solution5
from Problem2 import Solution as Solution2
from Problem206 import Solution as Solution206
from Problem234 import Solution as Solution234
from Problem448 import Solution as Solution448
from Problem543 import Solution as Solution543
from Problem617 import Solution as Solution617
from Problem15 import Solution as Solution15
from Problem17 import Solution as Solution17
from Problem19 import Solution as Solution19
from Problem48 import Solution as Solution48
from Problem215 import Solution as Solution215


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


def test_problem347():
    solution = Solution347()
    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 1)
    assert result == [1]

    result = solution.topKFrequent([1, 1, 1, 2, 3, 3, 3], 2)
    assert result == [1, 3]

    result = solution.topKFrequent([1, 2, 3], 3)
    assert result == [1, 2, 3]

    result = solution.topKFrequent([1, 1, 2, 2, 2, 3, 3, 3, 3], 1)
    assert result == [3]


def test_problem5():
    solution = Solution5()
    assert solution.longestPalindrome("aba") == "aba"
    assert solution.longestPalindrome("aa") == "aa"
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("abXYXwc") == "XYX"
    assert solution.longestPalindrome("abXYX") == "XYX"
    assert solution.longestPalindrome("abXYZYXwc") == "XYZYX"
    assert solution.longestPalindrome("abXYZYXYZYXwc") == "XYZYXYZYX"
    assert solution.longestPalindrome("mACAbdkACAa") == "ACA"
    assert solution.longestPalindrome("aacxycaa") == "aa"


def test_problem2():
    solution = Solution2()
    # 342+465=807
    result = solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8

    # 0+10=10
    result = solution.addTwoNumbers(ListNode(0), ListNode(0, ListNode(1)))
    assert result.val == 0
    assert result.next.val == 1

    # 0+0=0
    result = solution.addTwoNumbers(ListNode(0), ListNode(0))
    assert result.val == 0

    # 99+99=198
    result = solution.addTwoNumbers(ListNode(9, ListNode(9)), ListNode(9, ListNode(9)))
    assert result.val == 8
    assert result.next.val == 9
    assert result.next.next.val == 1


def test_problem206():
    result = Solution206().reverseList(ListNode(1, ListNode(2, ListNode(3))))
    assert result.val == 3
    assert result.next.val == 2
    assert result.next.next.val == 1
    assert not result.next.next.next

    result = Solution206().reverseList(None)
    assert not result

    result = Solution206().reverseList(ListNode(1))
    assert result.val == 1
    assert not result.next


def test_problem234():
    assert Solution234().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
    assert Solution234().isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))))
    assert not Solution234().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(0)))))
    assert Solution234().isPalindrome(ListNode(1, ListNode(2, ListNode(1))))
    assert not Solution234().isPalindrome(ListNode(1, ListNode(2, ListNode(3))))
    assert Solution234().isPalindrome(ListNode(1))
    assert not Solution234().isPalindrome(ListNode(1, ListNode(2)))
    assert not Solution234().isPalindrome(None)


def test_problem448():
    assert Solution448().findDisappearedNumbers([1, 2, 2]) == [3]
    assert Solution448().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert Solution448().findDisappearedNumbers([1, 1]) == [2]
    assert Solution448().findDisappearedNumbers([1, 2, 3, 4, 1, 2, 3, 4]) == [5, 6, 7, 8]


def test_problem543():
    assert Solution543().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3
    node_l = TreeNode(4, TreeNode(6), TreeNode(7, TreeNode(9)))
    node_r = TreeNode(5, None, TreeNode(8, TreeNode(10, None, TreeNode(11))))
    assert Solution543().diameterOfBinaryTree(TreeNode(1, TreeNode(2, node_l, node_r), TreeNode(3))) == 7
    assert Solution543().diameterOfBinaryTree(TreeNode(1)) == 0
    assert Solution543().diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1
    assert Solution543().diameterOfBinaryTree(TreeNode(1, TreeNode(2), TreeNode(3))) == 2
    assert Solution543().diameterOfBinaryTree(None) == 0


def test_problem617():
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    merged = Solution617().mergeTrees(t1, t2)
    assert merged
    assert merged.val == 3
    node = merged.left
    assert node
    assert node.val == 4
    assert node.left
    assert node.left.val == 5
    assert not node.left.left
    assert not node.left.right
    assert node.right.val == 4
    assert not node.right.left
    assert not node.right.right
    node = merged.right
    assert node.val == 5
    assert not node.left
    assert node.right
    assert node.right.val == 7
    assert not node.right.left
    assert not node.right.right


def test_problem15():
    result = Solution15().threeSum([-1, 0, 1, 2, -1, -4])
    assert result
    assert len(result) == 2
    expected = [(-1, -1, 2), (-1, 0, 1)]
    while len(result):
        r = result.pop()
        assert len(r) == 3
        assert r in expected

    assert not(len(Solution15().threeSum([])))

    assert not(len(Solution15().threeSum([0])))

    assert not(len(Solution15().threeSum([0, 1])))

    result = Solution15().threeSum([0, 0, 0])
    assert result
    assert len(result) == 1
    assert result.pop() == (0, 0, 0)

    result = Solution15().threeSum([1, 2, -2, -1])
    assert not(len(result))


def test_problem17():
    result = Solution17().letterCombinations("23")
    assert len(result) == 9
    assert set(result) == {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}

    assert not(len(Solution17().letterCombinations("")))

    result = Solution17().letterCombinations("9")
    assert set(result) == {"w", "x", "y", "z"}


def test_problem19():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    node = Solution19().removeNthFromEnd(head, 2)
    expected = [1, 2, 4]
    while node:
        expected_num = expected.pop(0)
        assert node.val == expected_num
        node = node.next
    assert not(len(expected))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    node = Solution19().removeNthFromEnd(head, 3)
    expected = [1, 3, 4]
    while node:
        expected_num = expected.pop(0)
        assert node.val == expected_num
        node = node.next
    assert not (len(expected))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    node = Solution19().removeNthFromEnd(head, 1)
    expected = [1, 2, 3]
    while node:
        expected_num = expected.pop(0)
        assert node.val == expected_num
        node = node.next
    assert not (len(expected))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    node = Solution19().removeNthFromEnd(head, 4)
    expected = [2, 3, 4]
    while node:
        expected_num = expected.pop(0)
        assert node.val == expected_num
        node = node.next
    assert not (len(expected))

    head = ListNode(1)
    node = Solution19().removeNthFromEnd(head, 1)
    assert not node


def test_problem48():
    matrix=[[1]]
    Solution48().rotate(matrix)
    assert matrix == [[1]]

    matrix = [[1,2],[3,4]]
    Solution48().rotate(matrix)
    assert matrix == [[3,1],[4,2]]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution48().rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution48().rotate(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


def test_problem215():
    assert Solution215().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution215().findKthLargest([3, 2, 1, 5, 6, 4], 3) == 4
    assert Solution215().findKthLargest([3, 2, 1, 5, 6, 4], 1) == 6
    assert Solution215().findKthLargest([3, 2, 1, 5, 6, 4], 4) == 3
    assert Solution215().findKthLargest([3, 2, 1, 5, 6, 4], 5) == 2
    assert Solution215().findKthLargest([3, 2, 1, 5, 6, 4], 6) == 1
    assert Solution215().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
