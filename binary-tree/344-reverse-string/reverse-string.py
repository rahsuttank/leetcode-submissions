class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(n // 2 + 1):
            s[i], s[n - i] = s[n - i], s[i]