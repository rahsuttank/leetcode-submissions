class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(s)
        newDig = []
        while len(digits) > 2:
            for i in range(len(digits) - 1):
                dig = ((ord(digits[i]) - 48) + (ord(digits[i + 1]) - 48)) % 10
                newDig.append(str(dig))
            digits = newDig
            newDig = []
        
        return digits[0] == digits[1]
        