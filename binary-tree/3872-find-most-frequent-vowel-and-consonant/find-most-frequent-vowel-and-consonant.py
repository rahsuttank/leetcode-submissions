class Solution:
    def maxFreqSum(self, s: str) -> int:
        ct = Counter(s)
        mxV = 0
        maxC = 0
        for key, val in ct.items():
            if key in "aeiou":
                mxV = max(mxV, val)
            else:
                maxC = max(maxC, val)

        return mxV + maxC
        