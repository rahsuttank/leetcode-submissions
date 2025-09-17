class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        res = 0
        arr.sort()
        for n in arr:
            if n == res:
                pass
            else:
                res += 1
        return res