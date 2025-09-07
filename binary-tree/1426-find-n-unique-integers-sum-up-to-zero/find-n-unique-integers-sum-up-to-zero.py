class Solution:
    def sumZero(self, n: int) -> List[int]:
        i = 0
        ans = [0] if (n % 2 != 0) else []
        while i < n//2:
            i += 1
            ans.extend([i, -i])
            
        
        return ans

        