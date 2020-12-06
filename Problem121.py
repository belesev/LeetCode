# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = len(prices)-1
        best = 0

        while left < right:
            candidate = prices[right] - prices[left]
            best = candidate if candidate > best else best

            # for left: next number is better buy price
            if prices[left+1] < prices[left]:
                left += 1
                continue

            # for right: previous  number is better sell price
            if prices[right-1] > prices[right]:
                right -= 1
                continue

            # move left if more profitable
            if prices[right] - prices[left+1] > prices[right-1] - prices[left]:
                left += 1
            else:
                right -= 1

        return best
