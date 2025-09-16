class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for row in range(n):
            for col in range(m):
                if row and col:
                    dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
                elif col:
                    dp[row][col] = grid[row][col] + dp[row][col-1]
                elif row:
                    dp[row][col] = grid[row][col] + dp[row-1][col]

        return dp[-1][-1]