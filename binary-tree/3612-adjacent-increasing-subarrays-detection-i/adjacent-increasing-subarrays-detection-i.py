class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        ct = k - 1
        if ct == 0:
            return True
        
        for i in range(k + 1, len(nums)):
            if nums[i] > nums[i - 1] and nums[i-k] > nums[i-k-1]:
                ct -= 1
                if ct == 0:
                    return True

            else:
                ct = k - 1
                i += k

        return False

        

        