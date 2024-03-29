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
from Problem88 import Solution as Solution88
from Problem125 import Solution as Solution125
from Problem31 import Solution as Solution31
from Problem98 import Solution as Solution98
#from Problem146 import LRUCache
from Problem56 import Solution as Solution56
from Problem98 import Solution as Solution98
from Problem133 import Solution as Solution133
from Problem133 import Node as GraphNode
from Problem199 import Solution as Solution199
from Problem211 import WordDictionary
from Problem173 import BSTIterator
from Problem438 import Solution as Solution438
from Problem238 import Solution as Solution238
from Problem304 import NumMatrix
from Problem621 import Solution as Solution621
from Problem721 import Solution as Solution721
from Problem863 import Solution as Solution863
from Problem863 import TreeNode as TreeNode863
from Problem986 import Solution as Solution986


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


def test_problem88():
    nums1 = [1, 3, 0, 0]
    Solution88().merge(nums1, 2, [2, 6], 2)
    assert nums1 == [1, 2, 3, 6]

    nums1 = [1, 2, 3, 0, 0, 0]
    Solution88().merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [0]
    Solution88().merge(nums1, 0, [7], 1)
    assert nums1 == [7]

    nums1 = [7]
    Solution88().merge(nums1, 1, [], 0)
    assert nums1 == [7]

    nums1 = [4, 5, 6, 0, 0, 0]
    Solution88().merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_problem125():
    assert not Solution125().isPalindrome("abc")
    assert not Solution125().isPalindrome("abcde")
    assert Solution125().isPalindrome("a")
    assert Solution125().isPalindrome("aba")
    assert Solution125().isPalindrome("abba")
    assert Solution125().isPalindrome("A man, a plan, a canal: Panama")
    assert not Solution125().isPalindrome("race a car")


def test_problem31():
    nums = [0, 1, 2, 5, 3, 3, 0]
    Solution31().nextPermutation(nums)
    assert nums == [0, 1, 3, 0, 2, 3, 5]

    nums = [1, 2, 3]
    Solution31().nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [1, 1, 5]
    Solution31().nextPermutation(nums)
    assert nums == [1, 5, 1]

    nums = [1, 5, 1]
    Solution31().nextPermutation(nums)
    assert nums == [5, 1, 1]

    nums = [1]
    Solution31().nextPermutation(nums)
    assert nums == [1]

    nums = [3, 2, 1]
    Solution31().nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [4, 3, 2, 1]
    Solution31().nextPermutation(nums)
    assert nums == [1, 2, 3, 4]


def test_problem98():
    assert Solution98().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
    assert not Solution98().isValidBST(TreeNode(1, TreeNode(2), TreeNode(3)))
    assert not Solution98().isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
    assert Solution98().isValidBST(TreeNode(2, TreeNode(1), TreeNode(5, TreeNode(3), TreeNode(6))))
    assert Solution98().isValidBST(TreeNode(2))
    assert Solution98().isValidBST(TreeNode(3, TreeNode(2, TreeNode(1))))
    assert Solution98().isValidBST(TreeNode(3, None, TreeNode(4, None, TreeNode(5))))


def test_problem199():
    assert Solution199().rightSideView(None) == []
    assert Solution199().rightSideView(TreeNode(1, TreeNode(2, TreeNode(3)))) == [1, 2, 3]
    assert Solution199().rightSideView(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))) == [1, 2, 3]
    assert Solution199().rightSideView(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == [1, 3, 5]
    assert Solution199().rightSideView(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))) == [1, 3, 5]
    assert Solution199().rightSideView(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5)),
                                                TreeNode(3, TreeNode(8)))) == [1, 3, 8, 7]
                                                
def test_problem146():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(2) == 2
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_problem56():
    assert Solution56().merge([[2,3],[1,3],[5,7],[4,6]]) == [[1,3], [4,7]]
    assert Solution56().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1,10]]
    assert Solution56().merge([[1,3], [2,4], [8,9]]) == [[1,4], [8,9]]
    assert Solution56().merge([[1,2], [3,4], [8,9]]) == [[1,2], [3,4], [8,9]]
    assert Solution56().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution56().merge([[1,4],[4,5]]) == [[1,5]]
    assert Solution56().merge([[1,4],[0,5]]) == [[0,5]]
    assert Solution56().merge([[0,5],[1,4]]) == [[0,5]]


def test_problem98():
    assert Solution98().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
    assert not Solution98().isValidBST(TreeNode(2, TreeNode(3), TreeNode(1)))
    assert Solution98().isValidBST(TreeNode(2, TreeNode(1)))
    assert Solution98().isValidBST(TreeNode(2, None, TreeNode(3)))
    assert not Solution98().isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))))


def test_problem133():
    node1 = GraphNode(1)
    node3 = GraphNode(3)
    node2 = GraphNode(2, [node1, node3])
    node4 = GraphNode(4, [node1, node3])
    node1.neighbors = [node2, node4]
    node3.neighbors = [node2, node4]
    clone1 = Solution133().cloneGraph(node1)
    assert clone1.val == 1
    assert len(clone1.neighbors) == 2

    clone2 = clone1.neighbors[0]
    assert clone2.val == 2
    assert len(clone2.neighbors) == 2

    assert clone2.neighbors[0] == clone1
    clone3 = clone2.neighbors[1]
    assert clone3.val == 3

    clone4 = clone1.neighbors[1]
    assert clone4.val == 4
    assert len(clone4.neighbors) == 2
    assert len(clone3.neighbors) == 2

    assert not Solution133().cloneGraph(None)

    single_node = Solution133().cloneGraph(GraphNode(3))
    assert single_node.val == 3
    assert not len(single_node.neighbors)


def test_problem211():
    obj = WordDictionary()
    obj.addWord('x')
    assert obj.search('x')

    obj.addWord('bad')
    assert not obj.search('b')
    assert obj.search('bad')
    assert not obj.search('sad')

    obj.addWord('sad')
    assert obj.search('sad')

    obj.addWord('foo')
    assert obj.search('.oo')
    assert not obj.search('.ox')

    obj.addWord('boo')
    assert obj.search('..o')
    assert obj.search('...')


def test_problem173_3nodes():
    iter = BSTIterator(TreeNode(2, TreeNode(1), TreeNode(3)))
    assert iter.hasNext()
    assert iter.next() == 1
    assert iter.hasNext()
    assert iter.next() == 2
    assert iter.hasNext()
    assert iter.next() == 3
    assert not iter.hasNext()


def test_problem173_left_left():
    iter = BSTIterator(TreeNode(3, TreeNode(2, TreeNode(1))))
    assert iter.hasNext()
    assert iter.next() == 1
    assert iter.hasNext()
    assert iter.next() == 2
    assert iter.hasNext()
    assert iter.next() == 3
    assert not iter.hasNext()


def test_problem173_right_right():
    iter = BSTIterator(TreeNode(1, None, TreeNode(2, None, TreeNode(3))))
    assert iter.hasNext()
    assert iter.next() == 1
    assert iter.hasNext()
    assert iter.next() == 2
    assert iter.hasNext()
    assert iter.next() == 3
    assert not iter.hasNext()


def test_problem173_7_nodes():
    iter = BSTIterator(TreeNode(7, TreeNode(3, TreeNode(1), TreeNode(5)), TreeNode(15, TreeNode(9), TreeNode(20))))
    assert iter.hasNext()
    assert iter.next() == 1
    assert iter.hasNext()
    assert iter.next() == 3
    assert iter.hasNext()
    assert iter.next() == 5
    assert iter.hasNext()
    assert iter.next() == 7
    assert iter.hasNext()
    assert iter.next() == 9
    assert iter.hasNext()
    assert iter.next() == 15
    assert iter.hasNext()
    assert iter.next() == 20
    assert not iter.hasNext()


def test_problem438():
    assert Solution438().findAnagrams("abab", "ab") == [0, 1, 2]
    assert Solution438().findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert Solution438().findAnagrams("", "a") == []


def test_problem238():
    assert Solution238().productExceptSelf([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert Solution238().productExceptSelf([-1, 0, 0, -3, 3]) == [0, 0, 0, 0, 0]
    assert Solution238().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_problem304_1():
    assert NumMatrix([[1,2,3], [4,5,6], [7,8,9]]).sumRegion(1,1,2,2) == 28


def test_problem304_2():
    assert NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]).sumRegion(2,1,4,3) == 8
    assert NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]).sumRegion(1,1,2,2) == 11
    assert NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]).sumRegion(1,2,2,4) == 12


def test_problem621_1():
    assert Solution621().leastInterval(["A","A","A","B","B","B"], 2) == 8


def test_problem621_2():
    assert Solution621().leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_problem621_3():
    assert Solution621().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16


def test_problem621_4():
    assert Solution621().leastInterval(["A", "A", "A", "B", "C", "C", "C"], 4) == 12


def test_problem621_5():
    assert Solution621().leastInterval(["J","I","A","D","E","B","J","I","H","H","B","H","H","A","E","A","H","B","C","E","B","B","B","D","D","A","F","D","E","B","J","D","C","F","E","I","C","D","E","C","H","A","H","F","E","B","G","I","J","F","H","D","F","H","E","C","I","G","E","A","G","E","J","A","F","G","G","E","H","B","B","E","H","E","H","E","I","E","A","G","E","B","E","G","I","F","B","B","D","B","F","A","F","E","I","B","F","D","J","H","A","C","I","E","E","D","F","C","C","G","A","B","A","H","B","I","H","A","E","C","I","F","E","H","B","I","J","A","A","D","G","I","C","A","A","B","D","D","D","I","I","I","F","D","I","C","G","E","A","B","G","A","C","C","C","J","H","H","E","I","I","D","B","E","E","H","C","A","H","E","E","H","I","C","I","B","I","J","G","D","J","G","A","H","B","B","B","J","D","J","B","F","G","C","E","H","G","G","J","H","A","I","C","H","D","C","H","E","C","I","I","F","E","I","D","D","H","A","I","F","F","F","B","I","D","I","J","E","C","B","D","C","D","I","G","B","J","G","E","D","D","J","B","A","E","F","D","J","D","G","C","G","C","A","F","F","G","G","E","G","A","J","B","I","H","E","I","I","E","H","I","H","C","D","A","E","B","J","H","B","D","C","D","C","C","A","B","G","A","B","E","D","G","I","C","B","J","D","D","E","B","G","E","H","F","H","H","E","C","H","J","G","D","J","C","J","G","B","G","A","I","I","B","D","G","D","E","B","H","G","F","E","A","B","F","G","B","D","J","C","E","A","A","B","D","J","C","C","E","G","H","I","D","G","B","G","C","E","A","C","A","E","F","F","G","C","H","C","H","I","J","J","B","B","B","B","J","H","I","B","I","F","C","G","B","B","G","A","H","D","D","F","I","A","H","E","E","I","I","H","C","C","F","H","I","C","J","A","I","G","E","F","J","J","C","I","G","B","A","C","B","G","J","H","D","F","B","D","G","J","I","C","G","H","E","F","F","B","J","I","B","C","J","G","F","B","G","C","A","E","F","E","E","F","J","I","D","D","B","I","C","G","C","G","C","A","J","J","F","I","E","E","A","I","B","H","C","H","H","D","A","F","E","D","C","H","C","D","D","E","F","B","C","F","I","F","G","I","B","H","I","A","E","A","A","E","F","B","I","B","H","E","J","J","H","C","H","D","B","C","I","G","F","D","C","F","G","G","B","J","A","H","B","H","J","D","D","D","A","D","I","H","A","B","G","H","C","F","E","A","I","H","F","G","I","B","F","E","C","J","C","A","E","G","H","D","C","B","H","F","B","B","J","E","D","I","A","D","F","H","H","H","C","D","A","I","F","F","D","E","F","E","C","C","D","G","J","C","C","A","C","H","C","H","J","F","G","C","A","A","E","H","B","H","G","F","B","H","H","D","C","C","H","G","I","H","H","J","B","D","J","F","I","D","I","H","G","D","B","E","G","F","D","E","D","J","B","D","G","H","F","A","D","G","E","E","D","A","I","D","G","J","F","I","I","C","I","E","B","A","A","E","H","G","G","H","H","G","F","G","H","A","J","G","H","G","D","J","I","D","I","E","D","A","B","G","B","G","D","J","I","C","C","H","G","J","C","H","I","C","E","G","I","F","H","J","E","H","F","I","G","B","E","G","D","J","J","D","C","B","F","E","B","H","F","D","H","B","F","C","A","D","I","D","I","B","J","C","B","H","C","E","F","G","A","F","B","G","I","D","A","F","F","A","E","H","A","J","B","C","G","E","E","B","G","J","H","G","C","I","A","F","D","H","J","J","C","F","F","C","J","E","I","B","A","A","A","G","G","H","G","D","J","J","E","E","H","D","J","C","J","E","B","J","A","I","I","D","H","J","I","C","C","G","A","I","G","E","J","A","I","F","H","D","E","C","A","A","I","J","G","F","B","J","J","B","D","D","E","B","F","H","C","G","F","H","G","D","E","F","J","A","F","J","B","F","F","C","E","C","E","I","D","A","B","C","B","D","J","C","C","I","D","I","I","E","A","I","H","B","E","E","A","C","C","F","E","E","G","D","J","J","J","J","A","C","F","B","D","J","G","E","F","G","F","F","G","J","C","D","H","A","A","C","A","I","F","C","F","I","G","H","I","G","B","J","F","J","D","F","F","E","J","B","I","H","D","J","B","A","C","A","A","H","F","F","E","J","J","F","E","B","J","B","E","C","B","I","D","F","C","D","I","I","G","I","D","G","E","B","J","E","A","G","A","A","E","G","J","C","E","I","F","H","J","I","E","A","C","B","B","D","I","I","J","J","E","A","F","E","J","G","I","B","G","J","J","I","E","A","J","F","G","C","J","A","C","I","G","G","E","A","C","J","C","J","D","G","F","H","E","F","D","B","J","H","C","E","E","C","A","D","G","I","C","C","H","D","D","A","D","F","H","F","I","G","D","E","D","J","B","C","J","I","C","H","C","B","C","A","B","F","A","J","A","A","C","J","F","G","B","D","D","B","I","C","E","H","C","J","E","F","A","A","J","F","H","E","H","E","I","F","B","C","H","A","C","D","G","G","H","J","A","H","F","F","I","B","I","B","D","H","D","B","J","I","D","D","D","D","G","E","B","E","H","I","J","B","I","G","H","B","C","D","B","D","J","E","H","C","J","F","G","I","F","J","D","C","F","I","H","D","D","I","C","B","E","F","J","A","D","J","J","J","H","F","J","H","A","E","B","B","D","I","C","D","D","E","B","F","D","A","D","G","D","F","F","I","J","I","I","E","G","C","H","I","D","J","G","H","I","I","G","E","C","G","J","J","H","F","A","J","B","C","E","B","I","C","C","D","J","G","F","J","D","C","J","F","J","J","C","I","H","B","E","F","A","G","A","D","H","B","I","F","E","D","C","I","C","F","I","J","G","B","D","I","J","A","I","C","G","A","E","G","E","F","B","C","D","E","J","E","C","G","F","D","B","B","D","B","A","C","D","F","C","J","F","D","F","E","F","F","G","J","E","J","C","G","B","F","I","C","F","J","I","B","G","D","I","E","J","D","J","A","G","B","A","B","G","E","G","A","C","G","G","J","C","I","F","H","G","D","E","C","J","C","J","D","D","G","J","C","D","G","A","F","H","A","B","F","E","G","A","F","G","C","I","H","A","H","J","H","B","D","E","I","G","I","F","I","G","E","F","A","H","G","F","A","A","F","F","B","E","G","F","B","F","J","J","E","J","D","I","G","D","J","C","F","G","G","G","H","B","D","C","H","G","J","F","A","C","H","E","F","A","J","D","C","C","G","A","F","J","B","J","B","B","C","J","A","C","A","H","I","J","D","D","B","A","B","D","H","F","C","E","E","B","D","H","E","G","B","F","J","A","B","C","G","F","H","I","B","F","D","D","I","E","D","A","C","F","J","B","G","C","G","J","I","E","H","H","F","E","B","I","H","B","J","F","H","H","B","I","C","G","F","H","J","C","A","H","H","G","E","C","C","D","C","E","D","G","G","H","B","H","D","A","C","J","A","H","E","G","C","H","H","D","I","F","G","F","A","A","B","D","E","H","G","B","C","D","J","H","F","H","I","J","E","C","C","G","H","I","I","H","B","H","J","E","C","I","F","J","H","F","D","I","B","G","H","D","E","F","F","A","D","G","B","A","A","E","H","J","J","H","F","E","E","E","B","F","G","J","B","G","C","C","F","C","B","D","B","A","B","H","I","H","E","D","A","F","I","B","F","H","C","D","I","G","F","J","H","F","I","A","A","D","C","B","H","G","G","B","J","F","J","G","E","G","G","C","A","C","C","F","H","F","D","A","E","D","H","I","I","H","I","I","F","E","H","G","D","H","I","H","C","E","C","F","I","C","B","J","B","J","F","D","B","A","C","B","F","B","D","I","G","I","E","E","I","F","C","E","J","G","D","I","E","G","C","F","F","D","A","G","G","J","D","J","E","D","E","C","B","H","F","D","H","D","D","C","J","B","I","H","H","G","D","I","D","A","D","E","E","B","F","F","I","H","D","B","J","F","A","C","D","F","G","F","E","I","G","H","J","F","D","G","B","I","C","D","E","B","A","B","D","J","E","D","H","D","H","A","J","A","D","B","F","H","D","E","I","G","E","E","J","G","J","A","G","I","J","J","J","J","J","G","A","A","G","J","F","H","A","F","G","J","D","G","E","F","B","B","D","H","B","G","G","E","J","J","I","H","I","J","I","A","G","G","G","I","J","I","D","F","B","D","I","J","I","E","J","F","B","C","A","H","B","E","I","I","B","E","C","H","J","H","H","B","D","A","D","J","C","F","A","D","G","E","F","I","F","D","F","G","H","A","H","A","C","I","J","A","H","E","D","G","D","A","F","B","G","A","I","G","J","C","G","F","F","H","D","D","D","I","F","G","G","D","I","C","A","C","E","B","F","J","D","J","F","E","E","C","B","H","J","G","J","E","A","A","E","I","D","H","D","C","C","A","G","I","E","H","G","H","C","D","B","G","B","G","I","B","E","H","F","F","D","H","C","H","F","H","F","D","J","D","F","I","A","H","J","H","D","G","A","G","E","J","J","F","D","F","E","D","C","I","D","C","A","E","I","D","B","E","A","I","J","J","F","C","C","F","G","F","B","D","D","A","E","I","H","B","E","G","C","D","D","J","I","F","I","J","A","B","F","I","D","I","F","H","D","H","D","H","B","C","C","D","D","J","A","J","J","C","H","H","C","B","C","G","F","E","A","C","C","J","H","I","A","D","C","A","D","D","H","H","H","J","G","E","F","H","C","J","F","G","I","I","E","A","C","B","E","F","F","C","A","G","F","E","I","F","E","E","D","B","H","H","F","G","E","J","D","I","B","F","H","E","A","J","B","J","B","C","I","B","G","A","C","F","C","F","F","F","J","J","D","G","J","A","H","B","A","F","H","G","E","A","G","F","H","G","E","D","F","H","F","B","D","C","A","H","A","G","C","F","E","F","F","A","F","E","A","D","G","D","A","E","A","I","B","G","E","E","G","J","E","C","C","H","D","A","E","B","G","C","C","D","E","E","A","B","E","G","D","F","A","F","H","I","I","E","F","H","F","H","C","B","C","F","G","D","G","I","E","C","I","I","E","G","B","E","F","G","H","G","C","J","C","A","D","G","C","G","I","F","B","A","B","I","C","G","B","D","H","C","I","B","I","J","G","B","F","H","F","D","E","J","C","D","B","G","B","J","A","E","A","C","D","J","H","E","D","J","E","I","B","J","J","J","C","E","A","D","E","I","E","I","J","J","C","C","I","B","I","H","F","I","G","A","H","J","C","H","G","I","A","A","J","D","G","A","J","I","A","A","H","G","J","A","E","G","E","D","A","D","I","F","F","J","H","I","I","B","H","I","D","C","A","C","D","F","C","A","F","F","G","E","B","B","B","G","D","B","E","H","A","C","D","H","F","D","I","F","C","I","H","E","E","D","D","A","B","G","F","F","A","B","I","J","D","A","A","B","J","J","J","C","H","F","I","J","D","A","E","F","H","A","G","D","D","J","G","F","B","B","H","D","H","F","G","E","B","G","D","B","E","E","F","J","C","F","D","A","F","I","C","I","G","D","E","F","G","E","J","F","G","B","I","F","J","J","H","G","I","E","G","C","G","E","F","J","G","I","B","C","G","C","A","D","D","F","B","D","E","H","B","J","A","A","E","C","G","C","I","B","D","D","D","H","I","J","D","C","D","I","E","G","E","J","B","F","A","J","A","G","D","H","F","I","A","F","J","H","I","G","D","B","J","G","J","F","B","H","I","F","H","J","H","I","A","J","B","I","J","B","D","C","G","D","J","E","D","J","D","C","B","F","F","H","J","J","B","H","J","D","D","C","F","A","I","A","F","F","I","D","B","E","E","F","G","C","B","I","E","C","F","J","J","E","G","G","A","I","F","E","I","A","G","H","A","D","C","A","I","C","G","E","B","G","D","I","H","J","D","H","A","J","F","F","F","B","C","C","F","D","I","G","D","B","F","F","G","A","G","B","E","H","F","E","G","E","I","I","F","G","F","C","B","D","H","J","G","A","F","E","G","F","C","F","I","J","E","C","A","G","H","J","C","A","H","C","C","I","C","A","A","B","G","D","F","E","F","F","I","J","D","D","J","H","G","H","J","B","H","C","D","B","A","B","H","A","I","F","C","B","F","I","F","H","H","C","B","D","C","J","I","I","F","B","C","C","G","A","A","A","A","H","A","J","H","H","J","C","D","B","B","J","H","E","J","C","C","E","G","F","H","F","J","B","E","C","I","B","D","J","G","H","J","I","A","A","F","A","A","H","F","C","B","C","F","J","I","C","E","J","D","H","D","F","H","I","G","I","B","B","H","A","A","A","E","B","G","E","I","G","F","G","C","H","A","H","H","H","F","J","F","B","G","D","B","G","D","C","E","H","H","A","A","G","B","C","I","H","E","E","F","B","C","G","J","E","F","B","J","B","E","D","D","C","J","G","I","I","G","G","H","D","G","F","C","H","G","E","D","F","D","E","I","E","I","I","I","J","H","I","A","D","D","B","E","H","B","B","C","E","C","D","J","J","F","G","B","E","D","F","I","C","J","J","F","C","J","E","J","G","H","F","A","C","C","B","I","I","F","G","F","F","H","J","E","D","I","I","E","A","J","C","H","I","B","A","G","J","B","H","E","B","J","J","B","F","J","G","I","H","B","I","J","J","E","H","E","H","E","E","G","H","E","G","B","A","D","H","I","J","J","F","F","E","I","C","A","I","E","D","F","A","I","J","H","H","G","G","J","G","D","A","D","J","B","G","H","D","E","J","A","A","B","C","J","F","J","E","A","H","J","F","F","H","J","I","J","E","H","B","A","H","J","G","I","G","F","E","D","I","D","H","B","J","D","E","C","A","C","G","J","I","D","F","C","D","D","H","F","A","H","D","J","B","G","J","I","G","J","I","I","J","J","C","G","F","B","I","H","C","B","H","J","A","A","H","B","J","G","C","G","G","I","E","A","H","E","C","E","D","J","D","A","J","E","G","F","I","H","J","G","H","F","I","F","D","F","C","B","C","H","G","F","I","J","D","C","B","I","I","J","A","F","A","F","E","H","J","J","C","B","B","A","A","C","A","I","C","G","A","I","I","D","A","C","I","E","D","H","E","I","H","C","J","C","D","I","B","D","J","F","H","J","D","I","G","I","I","I","E","G","H","D","D","I","E","B","D","G","A","G","I","D","D","C","C","F","F","J","H","E","I","D","B","C","F","H","D","F","C","B","I","I","E","A","E","J","D","I","H","A","I","F","G","I","B","J","D","I","G","H","H","A","J","D","D","C","F","E","B","A","A","I","I","H","D","C","A","B","I","B","I","F","H","F","J","C","G","G","I","D","I","I","F","J","A","I","B","I","D","D","G","D","C","D","H","B","B","A","B","I","F","J","C","D","D","B","G","B","C","D","F","A","D","E","D","J","E","C","G","H","I","I","F","I","A","E","J","F","I","B","D","C","B","D","H","B","F","B","J","H","J","J","A","B","C","I","F","B","E","G","G","E","B","D","H","D","I","E","H","I","A","E","J","D","J","F","D","G","C","F","C","G","C","B","B","F","G","H","B","A","C","D","A","J","A","B","E","C","A","C","C","C","B","C","I","A","E","E","F","B","G","I","G","C","G","I","G","J","E","C","J","F","I","D","C","G","J","J","C","E","A","F","H","H","G","D","G","B","J","G","I","I","I","A","B","B","E","J","D","I","H","G","H","H","C","I","G","F","H","J","I","H","B","G","B","C","G","H","C","H","I","C","A","E","E","C","E","C","G","D","A","G","I","G","F","H","E","C","G","G","J","D","E","F","E","H","E","G","F","E","G","G","A","E","J","H","F","I","J","J","F","F","B","B","J","I","G","G","B","F","G","F","G","E","D","E","A","B","B","J","J","E","F","C","A","F","E","J","B","B","A","C","A","F","A","F","D","B","F","C","H","H","E","I","H","H","A","B","E","A","A","G","C","E","G","D","A","F","C","F","B","E","G","H","A","D","I","I","B","F","C","D","E","B","G","B","I","A","C","H","A","G","D","F","B","D","J","F","C","C","I","J","G","A","A","B","I","C","D","F","D","E","C","F","I","B","C","F","H","I","E","D","F","I","I","D","B","E","G","H","E","D","I","A","E","C","E","D","C","C","F","C","A","A","H","E","A","C","D","E","H","F","C","A","C","B","H","A","I","D","E","D","E","A","B","F","I","C","H","J","C","B","A","C","H","H","G","B","J","F","C","F","F","F","E","G","D","B","A","I","C","H","F","J","H","A","D","D","C","F","E","C","F","B","G","C","G","J","A","C","F","I","D","E","E","D","D","E","F","E","B","J","C","I","D","D","H","J","A","A","H","H","H","J","I","G","C","G","D","C","J","C","H","G","E","E","C","E","F","F","E","H","H","C","G","C","I","I","I","H","G","F","A","H","G","H","B","A","A","E","C","J","F","J","E","H","H","D","I","F","B","G","I","E","F","E","A","F","C","H","G","B","F","A","G","F","F","F","F","B","A","J","J","G","I","H","C","J","G","G","I","C","F","H","J","E","C","D","H","E","C","C","F","I","G","H","F","D","F","B","E","I","C","D","B","H","J","G","I","I","A","F","E","A","G","H","B","J","F","J","C","B","C","G","I","J","I","J","F","J","H","B","G","E","H","C","B","G","A","D","J","F","I","B","D","F","H","H","A","C","H","J","C","C","I","D","F","F","I","E","C","G","J","D","B","F","F","H","F","C","C","H","A","G","E","D","C","A","J","J","B","D","J","B","J","B","D","G","B","G","B","G","G","J","I","B","F","C","E","D","D","A","I","E","E","H","J","J","E","F","H","C","D","D","E","J","H","E","E","D","H","B","F","E","J","E","I","G","B","D","H","J","D","C","G","I","I","I","J","I","G","H","J","F","A","D","G","I","A","E","G","C","F","J","E","E","A","A","D","J","H","A","I","F","F","A","D","I","E","G","D","B","D","C","D","A","E","E","C","D","E","I","G","A","D","D","A","B","F","B","D","B","B","J","E","E","I","G","A","B","B","E","J","B","G","B","F","J","G","C","D","C","H","I","H","F","F","A","H","E","B","D","E","A","I","D","I","E","A","I","I","F","H","B","D","C","E","G","I","J","J","D","E","A","C","C","E","D","F","C","F","F","I","E","H","F","J","C","H","E","C","G","H","C","C","E","A","J","J","C","F","H","J","G","B","G","G","G","F","G","J","C","G","J","E","G","B","I","H","H","C","G","B","A","I","I","J","H","H","B","B","C","D","C","H","I","J","D","F","H","J","A","G","H","E","A","B","H","A","I","F","I","I","G","B","J","D","I","C","A","A","G","B","F","G","F","B","H","I","A","F","H","I","C","D","E","A","A","I","I","J","E","J","H","J","D","F","D","E","E","F","E","A","G","B","J","I","D","I","H","D","E","E","B","A","C","J","C","D","B","I","H","F","B","J","B","A","D","F","G","F","G","J","A","D","E","C","B","G","J","D","B","E","I","I","E","G","I","D","J","I","A","F","H","B","A","C","B","I","J","D","J","I","J","A","G","F","B","E","H","A","D","F","D","F","I","D","D","D","D","I","B","F","H","I","G","J","I","C","F","G","H","J","J","J","E","A","G","G","C","A","G","F","J","C","B","H","E","H","C","F","G","C","H","A","H","D","H","J","B","G","C","F","H","J","H","J","C","C","I","I","F","G","I","C","A","D","H","E","D","F","E","H","F","H","E","A","F","E","B","C","E","G","I","G","J","E","I","G","B","C","G","C","F","J","B","G","B","G","J","A","D","C","B","B","D","E","B","I","F","A","A","A","I","D","F","I","D","A","E","E","B","A","I","E","H","C","C","G","D","J","A","H","H","H","A","D","A","C","G","H","F","G","E","H","G","E","F","H","B","A","E","E","G","G","D","F","I","D","F","F","J","F","J","C","B","H","B","G","D","C","C","E","G","H","H","J","I","I","A","F","D","C","A","J","F","E","A","H","I","B","G","E","F","J","I","F","A","B","G","B","C","F","C","B","G","E","G","A","G","B","H","E","B","D","C","F","B","E","C","H","I","A","F","C","C","J","H","J","F","E","C","I","F","J","G","E","G","A","B","C","D","D","F","G","E","H","H","I","C","E","F","A","H","I","A","C","C","H","E","H","C","F","H","B","H","G","E","E","G","E","I","E","H","J","F","F","D","B","A","F","B","I","A","D","J","G","I","G","B","D","J","E","D","B","J","H","C","F","A","C","J","F","I","A","J","I","H","G","I","J","C","I","B","F","C","G","C","E","F","G","I","I","A","G","A","H","I","C","F","G","H","G","C","F","B","C","H","H","I","F","A","C","F","J","I","A","J","F","A","D","F","G","F","E","H","F","I","F","J","F","F","G","D","G","B","C","A","G","F","H","J","G","D","C","E","I","A","F","J","C","H","H","G","C","A","G","J","C","H","B","C","D","G","C","C","E","B","A","B","F","I","A","J","F","G","H","H","A","G","B","A","D","F","A","I","C","E","J","H","J","J","G","J","D","I","A","B","B","C","B","H","F","D","F","G","B","G","B","A","E","D","D","A","D","G","J","G","F","H","J","A","J","E","J","F","C","D","B","F","G","C","C","H","B","F","I","A","J","C","F","B","I","E","D","B","I","G","B","C","B","J","F","I","E","F","F","H","B","I","F","J","H","I","C","F","H","H","A","J","A","F","G","B","H","F","A","B","G","B","H","F","G","J","H","D","J","J","A","H","F","F","C","D","I","H","A","G","H","B","G","D","B","I","D","E","J","C","D","D","H","I","A","B","C","B","C","B","H","E","C","I","A","F","A","G","H","G","I","C","E","A","D","B","H","F","J","E","D","E","F","B","G","F","F","D","E","J","I","H","C","G","I","I","D","I","H","F","I","D","H","I","C","J","A","A","C","F","B","A","G","I","I","J","B","E","B","A","H","H","J","A","F","H","E","C","E","I","J","C","C","A","B","J","J","A","E","H","J","C","J","A","D","C","H","J","E","C","G","G","D","E","H","A","A","E","F","C","G","H","D","H","E","B","E","B","I","E","C","J","A","D","A","J","D","D","C","B","D","G","F","F","I","D","I","E","B","E","E","F","C","A","J","A","E","I","B","J","E","F","J","D","E","C","H","A","B","J","C","E","I","G","G","J","D","B","B","H","D","A","J","A","F","E","H","H","C","F","B","J","G","I","J","H","C","F","A","C","B","F","C","H","G","B","F","F","F","D","A","C","B","J","H","I","B","G","F","H","C","F","E","F","B","D","G","C","G","G","D","H","H","F","H","J","A","H","A","H","E","H","H","E","H","D","C","A","A","C","D","F","J","F","H","H","D","A","H","F","G","E","D","A","D","D","G","A","F","E","D","A","G","C","A","A","G","E","I","H","E","F","F","I","E","F","A","A","C","A","I","B","I","I","A","B","H","E","D","A","A","J","A","J","I","J","I","D","H","F","C","F","I","I","G","F","E","H","H","F","G","G","B","F","B","G","I","D","D","I","E","H","C","C","J","C","I","G","F","F","B","F","J","B","B","F","H","F","F","F","G","C","B","D","C","B","J","C","G","D","C","I","G","A","A","I","J","F","F","A","D","E","C","C","E","C","J","J","G","J","F","B","A","H","C","B","B","D","B","G","E","E","B","F","E","E","C","F","B","H","E","C","G","D","A","I","G","I","F","C","D","G","D","F","D","C","C","F","F","H","I","I","G","G","G","G","A","J","D","F","D","F","A","A","H","G","G","I","C","I","G","H","G","B","C","B","A","F","D","J","G","C","G","E","C","E","J","F","B","G","A","H","B","D","C","G","I","D","F","A","C","C","C","A","B","E","C","F","J","B","D","B","A","J","A","A","B","H","H","D","J","B","C","J","B","D","G","G","G","F","C","C","A","F","I","A","C","I","J","I","H","G","C","A","J","H","G","H","C","A","H","J","F","I","B","C","B","D","I","G","D","G","D","J","C","D","E","D","I","J","B","J","H","I","F","C","B","F","I","D","B","H","A","E","C","D","C","B","A","F","C","J","C","E","E","E","D","I","H","B","I","E","H","E","D","D","J","A","H","G","C","E","H","I","J","C","J","A","J","G","G","C","E","B","I","D","C","D","C","B","J","F","J","J","A","G","C","B","D","J","G","I","J","E","G","B","G","C","F","G","F","H","J","I","I","G","C","G","C","G","B","G","H","D","F","F","F","C","E","C","C","I","D","A","F","G","C","B","A","E","A","F","G","J","H","D","B","C","J","D","I","J","D","G","A","C","A","I","I","D","H","G","I","F","H","I","J","E","C","B","H","J","D","G","I","B","B","H","B","C","B","I","H","I","G","A","I","I","I","F","D","I","H","A","F","G","B","I","E","C","F","B","H","I","D","B","G","A","I","E","E","D","A","J","J","E","B","I","F","I","B","E","A","F","C","E","H","B","H","F","I","J","I","D","H","A","B","A","A","J","F","B","I","F","E","E","E","H","B","B","F","H","A","G","H","F","F","B","F","D","A","C","B","J","A","H","H","F","I","E","E","H","D","D","D","A","C","H","F","F","G","B","I","E","B","E","C","B","E","J","H","I","C","D","E","A","B","D","G","F","I","I","B","I","A","C","B","G","C","A","A","H","E","H","D","D","D","G","D","D","E","C","B","E","I","B","F","E","B","F","J","C","C","H","C","B","E","D","C","C","I","A","H","C","A","I","J","F","H","D","B","H","I","I","F","I","B","B","F","D","A","E","G","G","E","H","A","A","I","H","D","H","E","I","E","D","G","G","B","H","I","F","C","I","G","J","J","I","H","D","D","H","D","J","F","G","E","B","J","J","D","C","B","I","C","F","B","F","E","G","A","A","F","I","C","H","A","D","B","C","J","C","B","G","C","E","G","J","H","A","C","B","A","I","E","E","J","G","E","A","H","D","H","J","C","H","E","H","F","J","J","B","D","E","H","D","G","A","B","E","I","D","I","B","F","C","C","D","A","E","J","D","I","E","F","J","A","I","F","B","J","J","C","H","F","H","I","E","J","G","A","B","F","C","C","E","H","I","G","F","F","A","C","A","G","E","A","E","J","A","I","C","G","F","H","F","J","I","F","B","I","A","E","D","I","J","B","F","B","C","A","F","B","H","F","E","I","C","J","G","C","H","C","G","A","B","C","F","H","B","A","G","F","F","J","H","A","E","E","F","B","F","G","C","H","H","B","B","A","I","B","H","G","J","H","F","A","A","J","D","D","H","D","E","B","A","I","J","C","H","C","D","G","G","B","H","F","E","F","C","F","E","J","B","H","J","J","E","F","F","J","G","C","D","H","G","F","E","E","D","G","E","F","I","C","J","B","I","E","C","C","G","H","D","B","C","I","E","J","F","E","J","E","J","B","D","E","E","G","F","J","C","G","F","G","E","B","A","B","F","C","E","F","E","E","F","C","F","B","H","D","D","E","I","I","D","A","D","D","C","E","B","H","E","A","B","A","C","A","G","B","H","D","F","J","D","F","H","G","E","B","J","H","J","E","I","B","C","B","F","I","J","F","G","I","C","B","D","C","F","J","H","E","D","H","J","G","E","I","J","C","A","H","B","I","A","J","I","F","E","F","C","H","F","C","B","B","E","B","F","B","H","I","G","D","E","G","F","I","J","B","F","A","F","H","J","E","H","F","E","H","C","E","I","E","A","B","B","D","G","D","E","G","B","H","G","B","D","F","H","C","H","C","I","E","A","G","B","A","I","B","D","B","G","E","G","C","G","C","J","I","J","B","G","D","I","F","D","F","A","D","A","F","E","I","F","I","G","B","H","E","C","A","A","J","B","J","B","H","H","D","C","B","E","E","D","E","A","B","F","B","H","J","A","B","A","J","D","H","C","A","G","F","H","A","H","A","H","C","D","D","G","F","B","H","C","C","G","D","F","A","H","A","D","D","C","B","E","I","J","D","H","F","E","B","A","C","E","E","E","C","G","I","J","E","H","A","A","A","J","B","F","I","F","D","D","G","F","E","B","J","E","J","C","F","A","I","H","I","G","D","J","F","I","H","E","B","H","C","I","G","B","G","C","B","J","J","B","H","I","C","H","C","H","A","A","H","J","H","J","F","J","F","B","D","I","D","B","B","G","B","D","G","D","B","B","F","I","G","E","B","E","B","F","E","H","F","B","F","C","G","D","H","G","H","H","C","I","J","C","B","D","C","A","G","G","B","I","I","B","E","D","B","A","G","G","J","G","A","J","C","I","E","E","F","J","H","E","C","A","G","F","E","G","E","I","J","F","C","E","C","J","G","D","H","C","J","A","D","G","A","G","E","G","G","A","I","J","E","E","E","B","H","C","I","J","B","I","B","F","A","A","I","G","H","D","I","G","J","B","H","G","B","H","B","I","D","G","D","F","D","A","D","D","B","F","J","A","E","J","G","F","F","H","H","I","H","C","E","D","I","B","F","C","H","C","I","A","C","A","E","J","G","A","C","D","A","G","F","F","D","F","G","C","F","I","B","A","H","G","F","F","A","J","C","C","F","H","E","G","D","G","B","E","E","D","C","G","H","I","J","J","E","I","B","B","D","B","A","F","A","J","J","D","J","F","H","D","F","B","I","B","F","E","D","D","J","A","G","G","C","B","I","C","A","D","B","D","C","F","B","D","F","B","A","J","H","E","D","B","J","E","A","C","C","J","A","I","G","C","A","G","F","I","G","I","G","A","B","G","F","J","D","E","I","B","C","C","C","F","H","I","F","E","C","C","D","D","A","G","E","A","H","I","F","E","F","J","B","F","B","E","D","G","E","G","I","H","A","I","E","G","E","D","C","D","C","B","F","B","D","J","B","B","G","E","A","J","G","H","J","J","C","J","F","C","C","E","A","A","E","H","A","F","G","H","E","B","G","B","D","J","I","B","J","E","B","E","G","A","G","J","D","I","G","C","I","F","C","H","H","F","J","C","J","D","D","I","A","B","F","G","J","I","G","G","G","F","I","I","C","F","E","C","A","B","D","D","J","C","D","A","A","G","E","B","E","G","J","D","I","H","B","A","A","H","G","I","D","B","A","A","H","I","J","E","D","G","H","H","J","A","H","G","J","B","C","F","G","F","I","F","J","A","G","B","E","C","C","C","I","J","H","A","D","H","B","B","A","H","H","D","C","C","G","A","G","H","B","E","C","A","D","H","H","D","B","H","I","D","A","F","E","D","H","C","C","A","F","E","F","C","B","B","A","C","C","H","B","I","J","E","E","C","G","H","H","C","C","D","I","D","D","H","B","D","H","F","C","H","G","D","I","I","E","F","E","J","B","I","J","H","I","I","B","E","F","I","A","C","A","B","I","G","J","H","J","C","B","C","F","D","I","D","A","F","H","I","A","D","H","F","J","F","I","H","J","G","E","B","J","E","A","G","B","I","J","I","C","D","A","D","C","B","C","I","J","I","F","I","J","E","B","H","E","G","B","A","D","D","H","B","I","J","E","G","G","E","A","I","I","H","H","G","D","E","A","B","D","C","A","J","H","C","A","C","H","A","B","E","H","A","E","H","I","G","B","G","C","C","B","E","H","H","H","C","I","B","C","F","A","F","C","F","F","F","C","D","C","C","G","C","A","F","B","G","D","F","D","F","C","G","D","E","H","G","B","D","B","G","C","H","J","B","E","J","J","J","E","D","F","G","G","B","I","E","F","H","E","I","J","G","D","C","A","G","H","B","H","A","H","I","J","A","D","J","E","F","J","D","F","E","C","H","G","D","E","C","J","H","J","A","I","D","G","I","J","I","A","F","F","D","J","F","I","H","C","B","B","J","J","H","E","I","D","E","J","J","C","D","H","D","J","I","E","J","E","J","E","J","J","B","C","D","B","I","A","F","D","G","E","E","H","E","E","E","I","I","B","H","D","C","A","J","H","E","I","F","B","G","I","C","B","A","F","C","H","D","H","J","B","J","F","H","E","D","E","C","E","G","B","J","D","D","A","I","F","A","I","I","D","C","I","F","H","C","I","B","H","J","H","J","G","G","E","A","E","E","I","B","A","I","H","G","D","J","D","A","C","B","F","E","F","I","E","B","E","H","D","B","I","G","E","G","J","I","H","F","G","B","G","D","F","A","G","D","F","E","A","B","H","C","H","G","B","I","J","E","H","I","C","F","H","B","J","C","A","E","D","B","A","F","F","G","J","C","D","G","B","A","H","G","G","J","F","G","H","I","I","C","D","C","E","E","I","H","C","G","I","A","E","G","H","F","H","D","B","F","A","D","I","E","H","E","C","A","A","I","J","F","G","C","I","E","G","C","A","E","H","J","G","I","G","D","I","E","F","C","J","D","H","J","H","E","D","J","A","B","A","A","F","H","J","A","J","B","A","E","E","G","A","C","I","C","E","C","A","G","F","F","B","B","C","A","A","H","I","C","I","D","B","B","H","G","C","D","F","G","E","A","E","F","I","G","F","H","J","E","E","E","G","B","B","B","A","C","G","C","G","E","C","F","E","G","F","E","E","A","G","F","D","J","D","F","J","J","H","J","I","G","B","E","I","B","C","D","G","G","B","B","B","G","E","I","E","J","I","E","D","D","F","D","A","H","I","D","C","B","B","J","F","H","G","C","C","B","A","C","C","H","H","C","J","F","D","A","H","A","B","I","A","D","H","E","E","I","G","J","G","I","E","J","A","I","J","F","C","H","H","C","F","I","J","I","D","G","D","B","H","I","H","A","A","E","E","I","C","A","E","I","F","A","J","G","E","C","H","I","B","J","H","F","F","D","D","J","J","C","J","G","A","H","E","I","A","I","F","J","I","B","H","I","G","I","D","H","B","I","C","I","H","H","C","H","C","D","A","J","B","D","C","E","F","D","D","A","F","F","B","A","H","H","E","J","H","E","B","B","E","B","J","C","F","H","H","C","D","F","G","J","D","D","J","I","J","B","F","A","J","C","I","F","I","G","I","E","I","D","J","A","A","D","B","F","I","D","D","C","F","H","G","E","E","F","D","A","I","I","B","I","E","E","B","A","C","B","D","F","I","A","A","B","J","H","E","F","J","I","D","F","B","I","F","H","D","F","F","I","B","C","F","B","A","B","G","D","E","G","B","A","E","H","I","J","C","D","E","B","H","I","J","F","C","F","H","H","G","I","B","D","D","E","H","E","C","C","D","C","D","B","B","A","J","J","H","G","D","G","I","I","D","B","H","J","I","I","C","G","I","I","H","G","E","E","J","H","F","H","C","I","G","I","H","J","C","I","J","G","C","B","A","B","J","G","E","I","G","I","A","A","G","H","I","C","C","A","C","I","E","H","A","D","E","J","C","H","C","H","E","C","I","D","G","D","E","J","C","B","E","H","J","H","H","I","B","D","I","C","I","J","H","I","B","C","E","D","C","C","D","E","D","E","G","G","C","J","D","C","D","A","I","H","A","E","D","J","H","G","G","A","B","F","B","I","E","A","C","I","C","F","E","J","J","B","I","H","I","H","D","D","E","D","J","I","I","E","D","A","F","G","E","A","B","E","B","A","I","C","E","C","H","E","C","E","J","D","B","D","C","G","I","C","F","A","D","H","F","B","A","C","C","H","H","J","D","I","E","E","H","J","F","B","E","D","E","G","I","J","B","D","E","D","H","F","H","H","B","G","B","G","B","G","A","H","J","A","D","G","E","D","I","F","E","D","G","C","D","G","F","B","C","B","H","I","B","G","I","B","D","J","I","E","C","D","D","E","I","B","H","J","B","D","E","D","G","B","J","D","B","D","A","D","G","H","B","D","I","A","E","B","I","J","D","B","C","F","J","F","F","B","B","E","I","D","F","A","A","C","A","J","J","B","D","A","G","F","C","I","E","F","F","F","J","D","H","C","C","C","A","D","I","J","H","I","I","H","J","E","B","A","A","E","H","A","D","B","J","E","F","J","A","E","I","H","H","I","G","J","E","D","I","A","H","J","H","B","J","B","H","B","I","E","G","C","J","C","I","A","D","I","C","J","B","G","I","B","J","H","F","D","H","C","I","I","H","A","C","G","I","C","G","I","B","I","F","H","I","E","A","F","C","D","C","F","J","H","D","I","D","A","A","D","A","A","B","B","I","I","D","G","B","A","B","A","G","B","A","B","H","B","E","G","B","E","I","B","A","A","A","F","J","D","D","F","E","G","J","F","A","I","G","J","C","E","H","E","I","D","B","H","H","C","I","I","J","A","E","E","F","I","E","A","D","I","E","E","I","B","A","I","A","C","I","B","I","B","H","C","A","B","B","B","H","E","J","A","G","A","C","D","G","F","G","I","A","G","F","G","I","A","E","J","D","B","D","E","A","B","F","G","E","I","A","A","B","A","H","H","H","H","B","B","C","E","E","F","E","A","J","E","J","I","D","A","C","I","I","E","A","C","B","J","D","J","D","F","C","G","A","H","F","J","E","B","H","F","D","J","F","F","F","I","H","D","F","F","H","G","I","H","C","I","D","C","J","I","A","G","D","E","E","C","E","G","H","A","C","J","I","H","J","B","B","J","E","D","C","I","J","F","B","B","E","G","E","F","I","D","C","J","E","G","C","J","D","G","G","B","F","G","I","J","A","I","B","H","H","J","H","H","C","D","A","G","E","D","I","B","A","A","C","F","F","B","J","E","B","J","G","B","B","J","I","B","H","I","E","C","I","H","F","H","E","J","H","C","E","E","I","G","D","J","G","D","A","H","E","F","H","G","G","C","B","E","F","I","G","F","A","H","C","E","B","G","C","I","B","A","I","H","J","G","F","A","I","J","J","I","J","I","H","I","F","D","G","A","D","F","J","I","G","C","C","C","I","I","B","E","B","E","A","I","C","D","J","E","H","F","F","B","J","D","C","F","I","C","B","G","H","J","I","I","I","A","H","C","B","B","E","A","D","B","J","J","J","F","F","J","G","A","I","H","I","C","D","A","G","J","G","J","B","D","D","E","D","F","A","D","C","F","D","G","J","H","C","A","A","E","F","J","B","F","H","B","C","B","B","A","G","I","I","G","J","C","G","I","I","A","E","J","G","F","A","J","G","D","B","I","C","I","E","I","H","D","F","B","H","B","D","A","G","C","E","C","G","F","E","E","E","A","H","H","I","F","F","C","I","G","I","H","D","I","G","H","I","A","A","C","G","I","D","A","E","C","H","F","B","E","J","J","E","I","J","I","J","C","G","J","J","D","A","D","H","E","I","I","J","F","G","F","G","D","D","B","J","A","A","J","A","I","H","J","C","D","E","D","B","J","F","E","C","F","F","C","I","E","H","J","J","H","C","F","A","C","J","J","H","J","G","H","E","J","J","D","E","G","H","I","E","I","H","A","C","E","D","E","F","A","A","G","G","B","C","C","A","E","C","C","B","H","F","I","I","C","H","A","I","J","G","H","C","J","F","J","C","B","E","E","E","E","F","J","H","C","B","H","H","J","J","C","E","B","J","A","I","C","E","D","F","E","D","E","B","F","J","B","H","F","D","H","B","J","D","H","G","I","C","H","I","J","G","B","J","H","B","D","C","G","C","F","D","F","H","E","H","H","I","E","G","H","D","A","G","F","G","J","H","C","C","I","A","J","D","I","C","B","B","H","C","D","F","A","G","H","D","E","A","I","A","C","F","G","C","J","E","D","G","B","G","J","J","D","D","J","C","J","F","H","C","C","J","G","E","C","H","A","D","G","F","J","A","H","H","C","B","B","C","H","G","J","H","E","J","D","F","A","A","D","D","H","D","C","E","H","H","B","B","B","F","C","C","E","G","B","H","H","A","G","D","H","I","B","C","H","C","H","D","F","E","J","H","J","D","D","E","A","D","A","H","G","C","G","D","B","D","D","F","B","D","I","A","C","A","D","D","C","H","G","I","B","F","B","E","I","H","F","A","J","A","C","D","C","J","D","A","D","G","C","C","C","F","E","I","I","F","J","D","H","J","C","E","A","B","A","H","A","A","C","C","F","D","D","B","D","A","A","B","A","G","G","D","J","I","B","C","I","B","H","F","H","F","E","H","F","G","F","C","A","B","J","B","A","D","D","I","F","I","B","I","F","E","H","A","C","E","H","B","E","J","C","H","C","C","E","A","E","I","A","I","G","D","J","A","D","A","A","G","J","A","B","H","D","C","I","I","J","D","I","D","A","F","B","H","A","H","I","F","B","G","I","A","G","B","H","B","D","C","E","C","B","E","J","C","H","E","I","B","D","H","F","D","D","B","D","I","F","D","C","H","F","F","D","A","F","H","D","H","A","D","A","G","G","B","C","A","I","E","C","I","J","F","E","H","A","H","G","F","I","B","B","I","H","E","B","G","J","C","A","B","G","G","H","A","E","G","E","B","E","D","E","E","A","A","A","D","E","E","J","F","D","B","D","C","I","B","H","G","C","J","B","I","G","B","I","F","J","F","H","F","E","E","A","H","D","E","B","G","I","A","D","G","H","I","J","A","G","H","F","D","D","J","I","I","G","E","J","G","E","H","D","D","A","F","C","D","G","I","B","E","G","A","J","A","J","D","A","G","J","E","A","F","D","A","G","E","C","A","D","E","J","E","H","J","C","B","C","B","H","I","I","H","D","G","F","G","D","F","B","C","E","G","H","C","J","A","B","D","H","C","G","J","C","I","D","C","H","E","A","D","B","A","E","G","E","B","C","F","J","F","D","B","I","H","D","F","C","H","H","H","B","B","C","F","J","D","C","A","I","I","I","B","G","F","B","C","C","I","B","E","A","I","H","C","H","J","F","B","C","J","D","F","F","F","J","E","H","C","A","J","I","E","D","B","F","C","D","B","D","A","I","C","E","F","D","F","E","H","J","C","H","C","I","J","J","B","E","F","C","B","G","B","C","B","H","E","E","F","H","I","J","I","B","E","G","D","H","I","F","J","D","I","A","B","C","C","J","D","C","I","G","D","B","E","H","I","I","A","J","A","E","D","J","J","I","E","E","G","H","C","A","E","D","H","F","I","A","A","J","D","B","G","E","B","H","J","D","J","I","J","A","D","I","D","F","C","D","J","A","B","C","B","H","I","G","H","F","A","C","G","A","H","B","H","E","C","B","J","E","C","F","D","E","G","I","D","J","C","A","H","I","J","C","D","A","F","D","C","G","I","C","J","B","I","G","D","J","B","G","J","D","G","I","E","A","D","I","I","I","G","H","I","A","C","I","D","E","E","A","E","C","G","E","H","E","E","I","G","J","F","C","C","C","B","B","G","I","H","I","A","F","I","F","J","G","C","H","H","J","I","F","G","H","A","D","B","H","C","I","B","B","D","G","H","F","F","G","A","E","B","I","E","D","C","H","H","I","E","D","B","F","A","J","A","C","J","E","G","A","G","D","F","J","A","G","F","D","I","I","E","G","G","C","F","E","I","H","J","J","B","J","H","H","E","D","H","F","A","H","I","J","J","F","F","E","E","E","C","I","G","F","B","C","H","C","C","A","I","A","J","A","F","J","A","J","J","C","B","F","F","D","G","F","F","I","I","E","G","A","A","C","H","C","G","J","C","J","I","A","D","F","F","A","H","D","B","I","A","C","J","B","B","C","F","I","G","E","J","I","I","F","J","J","F","F","A","A","E","H","B","C","J","C","B","A","B","H","G","A","E","D","I","A","C","G","C","G","D","A","E","D","E","J","F","G","G","H","F","G","G","G","F","B","G","F","G","J","A","H","C","D","G","J","H","E","A","C","D","C","B","B","J","D","B","J","G","C","D","D","A","B","C","B","C","A","H","D","A","G","C","I","G","A","I","B","G","E","C","G","G","D","I","D","A","F","H","F","C","H","I","I","A","H","I","A","I","I","D","B","J","E","D","I","G","E","D","C","J","D","G","A","J","J","A","A","A","C","A","D","H","H","F","C","G","J","F","I","E","I","I","I","E","I","B","H","H","A","H","I","H","J","J","J","F","H","A","I","A","D","H","A","I","I","I","E","G","C","E","D","B","E","F","J","J","B","D","C","G","A","D","J","D","I","B","J","F","D","C","J","A","B","H","G","G","I","A","F","J","C","C","F","H","B","G","J","A","F","G","E","H","G","J","J","G","H","C","D","C","C","A","J","G","H","J","E","D","H","F","F","J","A","F","I","G","C","C","A","E","D","D","I","H","F","D","F","G","D","B","J","E","J","F","D","F","B","E","J","D","F","D","H","G","E","D","H","D","A","J","B","H","E","A","E","H","F","I","I","G","A","G","H","A","C","D","I","B","G","H","H","A","G","B","D","J","E","J","I","G","B","D","B","H","D","A","F","B","H","H","D","G","B","G","E","B","G","H","D","B","H","G","F","E","E","E","I","J","J","G","G","F","H","E","I","H","H","F","I","C","F","B","H","F","B","F","E","G","D","A","F","B","J","J","C","I","B","D","F","B","F","F","G","B","I","A","F","D","F","G","B","B","C","F","D","J","H","F","F","E","D","D","E","C","J","C","F","F","C","F","G","C","F","I","B","H","A","A","I","G","H","A","E","A","I","E","E","I","J","I","H","D","J","B","H","J","F","H","E","F","F","F","E","C","G","E","F","A","D","F","H","J","D","J","F","H","J","H","J","J","D","D","G","B","F","D","D","C","A","D","C","E","G","F","A","C","G","B","C","I","E","I","B","J","E","D","D","E","J","C","D","I","C","G","C","G","H","C","E","G","A","H","A","D","C","D","J","D","I","A","J","J","G","G","A","E","C","A","H","F","F","D","I","H","J","A","C"], 63) == 100


def test_problem721_1():
    assert Solution721().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]) == [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


def test_problem863_1():
    target = TreeNode863(2, TreeNode863(3), TreeNode863(4))
    root = TreeNode863(1, target, TreeNode863(5, TreeNode863(6), TreeNode863(7)))
    assert set(Solution863().distanceK(root, target, 1)) == set([1, 3, 4])


def test_problem863_2():
    target = TreeNode863(5, TreeNode863(6), TreeNode863(2, TreeNode863(7), TreeNode863(4)))
    root = TreeNode863(3, target, TreeNode863(1, TreeNode863(0), TreeNode863(8)))
    assert set(Solution863().distanceK(root, target, 2)) == set([1, 7, 4])


def test_problem986_1():
    assert Solution986().intervalIntersection([[0, 2]], [[1, 3]]) == [[1, 2]]


def test_problem986_2():
    assert Solution986().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


def test_problem986_3():
    assert Solution986().intervalIntersection([[1,3],[5,9]], []) == []

