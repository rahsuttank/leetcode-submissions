class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l = 0
        r = len(s) - 1
        sList = list(s)
        while l < r:
            while sList[l] not in vowels and l < r:
                l += 1
                # print(sList[l])
            while sList[r] not in vowels and l < r:
                r -= 1
                # print(sList[r], r)
            sList[r], sList[l] = sList[l], sList[r]
            # print(sList)
            l += 1
            r -= 1
            # print(l, r, "lr")
        
        # print(sList)
        
        return "".join(sList)
        