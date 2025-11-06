class Solution:
    def maxDifference(self, s: str) -> int:
        ct = Counter(s)
        minEven = float('inf')
        maxOdd = 0
        for x in ct.values():
            if x % 2 == 0:
                minEven = min(minEven, x)
            else:
                maxOdd = max(maxOdd, x)
        
        return maxOdd - minEven