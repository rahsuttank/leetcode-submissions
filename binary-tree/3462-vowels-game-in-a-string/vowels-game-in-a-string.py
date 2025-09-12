class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        vCt = 0
        for c in s:
            if c in vowels:
                vCt += 1

        if vCt == 0:
            return False
    
        return True

        