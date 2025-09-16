class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)  # work in place
        count = [0] * len(s)  # parallel counts
        i = 0  # write pointer

        for j in range(len(s)):  # read pointer
            s[i] = s[j]
            if i > 0 and s[i] == s[i - 1]:
                count[i] = count[i - 1] + 1
            else:
                count[i] = 1

            if count[i] == k:  # remove last k chars
                i -= k
            i += 1

        return "".join(s[:i])
