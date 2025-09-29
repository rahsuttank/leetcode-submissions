class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [float("-inf")] * len(nums)

        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])
            ans = max(ans, cur_max)

        return ans
        