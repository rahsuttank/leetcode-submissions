from typing import List
from math import log, ceil

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def total_steps(l: int, r: int) -> int:
            steps = 0
            k = 1
            start = 1
            while start <= r:
                end = 4**k - 1
                range_start = max(l, 4**(k-1))
                range_end = min(r, end)
                if range_start <= range_end:
                    steps += k * (range_end - range_start + 1)
                k += 1
                start = 4**(k-1)
            return steps

        total_ops = 0
        for l, r in queries:
            steps = total_steps(l, r)
            total_ops += ceil(steps / 2)
        return total_ops
