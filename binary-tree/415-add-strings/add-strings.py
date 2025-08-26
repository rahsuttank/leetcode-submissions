class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        l1 = len(num1)
        l2 = len(num2)
        s1 = l1 - 1
        s2 = l2 - 1
        ans = []
        while s1 >= 0 or s2 >= 0 or carry:
            digit1 = int(num1[s1]) if s1 >= 0 else 0
            digit2 = int(num2[s2]) if s2 >= 0 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            ans.append(str(total % 10))

            s1 -= 1
            s2 -= 1
        
        return "".join(ans[::-1])



        