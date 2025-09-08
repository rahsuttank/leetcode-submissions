class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # ans = []
        def hasZero(num):
            return "0" in set(str(num))
        for i in range(1, n):
            if not hasZero(n - i) and not hasZero(i):
                return [i, n-i]

        