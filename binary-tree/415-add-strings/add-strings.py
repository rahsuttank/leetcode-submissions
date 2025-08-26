class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        s1 = len(num1) - 1
        s2 = len(num2) - 1
        ans = []
        while s1 >= 0 or s2 >= 0 or carry:
            digit1 = ord(num1[s1]) - ord("0") if s1 >= 0 else 0
            digit2 = ord(num2[s2]) - ord("0") if s2 >= 0 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            ans.append(str(total % 10))

            s1 -= 1
            s2 -= 1
        
        return "".join(reversed(ans))



        