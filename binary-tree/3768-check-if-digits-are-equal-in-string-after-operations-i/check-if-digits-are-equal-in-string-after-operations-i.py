class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(s)
        newDig = []
        while len(digits) > 2:
            for i in range(len(digits) - 1):
                dig = (int(digits[i]) + int(digits[i+1])) % 10
                newDig.append(str(dig))
            digits = newDig
            newDig = []
        
        # print(digits)
        return digits[0] == digits[1]
        