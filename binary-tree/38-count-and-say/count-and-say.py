def ct(num):
    ct = 1   
    ans = [] 
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            ct += 1
        else:
            ans.append([str(ct), num[i]])
            ct = 1
    ans.append([str(ct), num[-1]])
    return conct(ans)

def conct(s):
    ans = ""
    for c in s:
        ans += "".join(c)
    return ans

class Solution:
    def countAndSay(self, n: int) -> str:
        rle = '1'
        for _ in range(n - 1):
            rle = ct(rle)

        return rle
        