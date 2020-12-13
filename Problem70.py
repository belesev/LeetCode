# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        i = 2
        while i < n:
            # amount of way to the current stair =
            #            amount of ways to '-2' stair (and 2 stairs jump to the current)
            #          + amount of ways to '-1' stair (and 1 stair jump to the current)
            arr.append(arr[i-1] + arr[i-2])
            i += 1
        return arr[n-1]