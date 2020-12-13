# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices):
            return 0
        # array stores for each element the minimum value previous to it
        arr_mins = [prices[0]]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] - arr_mins[i-1] > max_profit:
                max_profit = prices[i] - arr_mins[i-1]
            arr_mins.append(min(arr_mins[i-1], prices[i]))

        return max_profit
