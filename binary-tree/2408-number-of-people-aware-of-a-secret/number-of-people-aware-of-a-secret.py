class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = pow(10, 9) + 7
        memo = [1] + [0]*(n-1)
        share = 0

        for i in range(1, n):
            share = (share + memo[i-delay] - memo[i-forget]) % mod
            memo[i] = share
        return sum(memo[-forget:]) % mod