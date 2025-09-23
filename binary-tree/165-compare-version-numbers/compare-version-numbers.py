class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1 = 0
        l2 = 0
        while l1 < len(v1) or l2 < len(v2):
            t1 = int(v1[l1]) if l1 < len(v1) else 0
            t2 = int(v2[l2]) if l2 < len(v2) else 0
            if t1 > t2:
                return 1
            elif t1 < t2:
                return -1
            l1 += 1
            l2 += 1
        return 0


        