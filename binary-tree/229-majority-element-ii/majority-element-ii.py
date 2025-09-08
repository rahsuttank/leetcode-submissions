class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ct = 0
        # can = nums[0]
        # ans = []
        # n = len(nums)
        # for i in range(1, n):
        #     if ct == 0:
        #         can = nums[i]
        #         ct = 1
        #     else:
        #         if can == nums[i]:
        #             ct += 1
        #         else:
        #             ct -= 1
            
        #     if ct >= n//3:
        #         ans.append(nums[i])
        # return ans
        ct = Counter(nums)
        n = len(nums)   
        ans = []
        for k, v in ct.items():
            if v > n/3:
                ans.append(k)

        return ans         

        