class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vCt = 0
        for c in s:
            if c in "aeiou":
                vCt += 1

        if vCt == 0:
            return False
    
        return True

        