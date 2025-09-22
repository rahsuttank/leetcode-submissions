class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ct = Counter(nums)
        maxF = max(ct.items(), key = lambda x: x[1])[1]
        ans = 0
        for key, f in ct.items():
            if f == maxF:
                ans += f
        
        return ans
        