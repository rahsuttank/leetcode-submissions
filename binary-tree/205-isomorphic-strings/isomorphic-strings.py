class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hsh = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in hsh and t[i] not in used:
                hsh[s[i]] = t[i]
                used.add(t[i])
            elif hsh.get(s[i], "") != t[i]:
                return False
        
        return True

        