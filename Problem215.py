# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
# not the kth distinct element.
#
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_queue = []

        for i in range(len(nums)):
            elem = nums[i]
            if len(max_queue) < k:
                self.__insert(max_queue, elem)
            elif elem > max_queue[0]:
                self.__squeeze(max_queue, k, elem)

        return max_queue[0]

    def __insert(self, max_queue: List[int], new_elem: int):
        # look for appropriate place
        i = 0
        if len(max_queue):
            while i < len(max_queue) and new_elem > max_queue[i]:
                i += 1
        max_queue.insert(i, new_elem)

    def __squeeze(self, max_queue: List[int], k: int, new_elem: int):
        if len(max_queue) >= k:
            # remove first element
            max_queue.pop(0)

            # look for appropriate place
            self.__insert(max_queue, new_elem)
