from typing import List

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # On day 1, 1 person knows the secret

        for i in range(1, n + 1):
            for j in range(i + delay, min(n + 1, i + forget)):
                dp[j] = (dp[j] + dp[i]) % MOD

        # People who still remember the secret on day n:
        ans = 0
        for i in range(n - forget + 1, n + 1):
            ans = (ans + dp[i]) % MOD
        return ans
