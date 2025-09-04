class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        
        ans = []
        for num in nums2:
            if num in count:
                ans.append(num)
                if count[num] == 1:
                    del count[num]
                else:
                    count[num] -= 1
        return ans
        