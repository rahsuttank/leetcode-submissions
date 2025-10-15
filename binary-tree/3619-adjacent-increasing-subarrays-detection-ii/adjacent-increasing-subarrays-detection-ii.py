class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        left = [1] * n  # length of increasing subarray ending at i
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1

        right = [1] * n  # length of increasing subarray starting at i
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(left[i], right[i + 1]))

        return ans
