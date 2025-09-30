class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            res += num * comb(n-1, i) 

        return res % 10
