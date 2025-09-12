class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("AEIOUaeiou")
        vCt = 0
        for c in s:
            if c in vowels:
                vCt += 1

        if vCt % 2 == 1 or (vCt % 2 == 0 and vCt != 0):
            return True
    
        return False

        