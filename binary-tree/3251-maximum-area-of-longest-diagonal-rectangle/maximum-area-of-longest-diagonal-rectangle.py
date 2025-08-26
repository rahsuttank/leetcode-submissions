class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea = 0
        maxDiag = 0
        for l, w in dimensions:
            tmpDiag = math.sqrt(l**2 + w**2)
            if tmpDiag == maxDiag:
                maxArea = max(maxArea, (l*w))
            elif tmpDiag > maxDiag:
                maxArea = (l*w)
                maxDiag = tmpDiag
            # maxDiag = max(maxDiag)
            
        
        return maxArea