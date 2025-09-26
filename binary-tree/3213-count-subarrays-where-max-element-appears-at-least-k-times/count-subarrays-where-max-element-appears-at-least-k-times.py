from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEl = max(nums)
        n = len(nums)
        start = 0
        ct = 0
        ans = 0

        for i in range(n):
            if nums[i] == maxEl:
                ct += 1

            while ct >= k:  # shrink left
                if nums[start] == maxEl:
                    ct -= 1
                start += 1

            ans += start   # all valid subarrays ending at i

        return ans
