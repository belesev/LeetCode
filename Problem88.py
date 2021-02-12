# https://leetcode.com/problems/merge-sorted-array/
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size
# equal to m + n such that it has enough space to hold additional elements from nums2.
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        buffer = []

        index1 = 0
        index2 = 0

        while index1 < m or index2 < n or len(buffer):
            best_found = False
            if index1 < m:
                best = nums1[index1]
                best_found = True
            if index2 < n and (not best_found or nums2[index2] < best):
                best = nums2[index2]
                best_found = True
            if len(buffer) and (not best_found or buffer[0] < best):
                best = buffer[0]

            # simply shift index1 if the best is from nums1
            if index1 < m and nums1[index1] == best:
                index1 += 1
                continue
            elif index2 < n and nums2[index2] == best:
                # save from nums1 to the buffer
                if index1 < m:
                    buffer.append(nums1[index1])
                # replace in nums1
                nums1[index1] = best
                index1 += 1
                # and shift pointer in nums2
                index2 += 1
            elif len(buffer) and buffer[0] == best:
                # save from nums1 to the buffer
                if index1 < m:
                    buffer.append(nums1[index1])
                # replace in nums1
                nums1[index1] = best
                index1 += 1
                # and shift pointer in buffer
                buffer.pop(0)
