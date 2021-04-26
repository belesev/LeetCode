# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
import math
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cumulated = 0
        sum_moded = []

        # [4,5,0,-2,-3,1]  -->  [4,4,4,2,4,0]
        for i in range(len(A)):
            cumulated += A[i]
            cumulated = (cumulated + K) % K
            sum_moded.append(cumulated)

        # считаем кол-во под-массивов, сумма которых имеет в остатке значения, которое в ключе
        # 4: 4pc.
        # 2: 1pc.
        # 0: 1pc.
        cnt = dict()
        for i in range(len(sum_moded)):
            some_mod = sum_moded[i]
            cnt[some_mod] = cnt.get(some_mod, 0) + 1

        # кол-во сочетаний значений с одинаковым остатком = сумма арифм. прогрессии i*(i-1)/2
        result = 0
        for (some_mod,same_mod_count) in cnt.items():
            if same_mod_count > 1:
                result += same_mod_count * (same_mod_count-1) / 2

        # плюс кол-во элементов, у которых остаток сразу равен 0, т.е. с начала массива до этой точки сразу делится на K
        result += cnt.get(0, 0)

        return math.floor(result)

