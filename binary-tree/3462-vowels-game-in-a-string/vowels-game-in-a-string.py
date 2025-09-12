class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "AEIOUaeiou"
        vCt, sCt = 0, 0
        for c in s:
            if c in vowels:
                vCt += 1
            else:
                sCt += 1
        if vCt % 2 == 1:
            return True
        elif vCt % 2 == 0 and vCt != 0:
            return True
        
        # if () or vCt == 1:
        #     return True

        return False

        