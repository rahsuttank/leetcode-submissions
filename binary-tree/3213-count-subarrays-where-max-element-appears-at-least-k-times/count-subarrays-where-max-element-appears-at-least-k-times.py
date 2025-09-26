class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEl = max(nums)
        n = len(nums)
        start = 0
        ct = 0
        ans = 0
        i = 0
        while i < n:
            if nums[i] == maxEl:
                ct += 1
            while ct >= k:
                if nums[start] == maxEl:
                    ct -= 1
                start += 1
            ans += start
            i += 1
        return ans



        