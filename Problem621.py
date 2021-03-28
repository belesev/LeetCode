# https://leetcode.com/problems/task-scheduler/
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different
# task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could
# complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same
# letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = dict()
        cooldown = dict()
        result = 0

        for i in range(len(tasks)):
            task = tasks[i]
            if task in counters:
                counters[task] += 1
            else:
                counters[task] = 1
                cooldown[task] = 0

        while len(counters):
            (next_task, price) = self.choose(counters, cooldown)
            print("next: " + next_task)
            if price > 0:
                self.make_step(counters, next_task)
                self.cool_down(cooldown, next_task, n)
            else:
                self.cool_down(cooldown, None, n)
            result += 1

        return result

    def choose(self, counters, cooldown) -> str:
        best = ("", 0)
        for (k, v) in cooldown.items():
            if v > 0:
                continue

            if k in counters and counters[k] > best[1]:
                best = (k, counters[k])

        return best

    def make_step(self, counters, next_task):
        counters[next_task] -= 1
        if counters[next_task] == 0:
            counters.pop(next_task)

    def cool_down(self, cooldown, next_task, n):
        for k in cooldown.keys():
            if k == next_task:
                cooldown[k] = n
            else:
                cooldown[k] = max(0, cooldown[k]-1)
