class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vCt = 0
        for c in s:
            if c in "aeiou":
                return True

        return False

        