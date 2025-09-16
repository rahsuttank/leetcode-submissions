class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk:
                if c == stk[-1][0]:
                    stk[-1][1] += 1
                    if stk[-1][1] == k:
                        stk.pop()
                else:
                    stk.append([c, 1])
            else:
                stk.append([c, 1])
        return "".join([x[0] if x[1] == 1 else x[1]*x[0] for x in stk])
                    