class Solution:
    def maxDifference(self, s: str) -> int:
        ct = Counter(s)
        # maxEven = max([x for x in ct.values() if x % 2 == 0])
        maxEven = 0
        minEven = float('inf')
        maxOdd = 0
        minOdd = float('inf')
        for x in ct.values():
            if x % 2 == 0:
                # maxEven = max(maxEven, x)
                minEven = min(minEven, x)
            else:
                maxOdd = max(maxOdd, x)
                # minOdd = min(minOdd, x)
        
        return maxOdd - minEven