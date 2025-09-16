class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # dp = [[0] * m for _ in range(n)]
        # dp[0][0] = grid[0][0]
        for row in range(n):
            for col in range(m):
                if row and col:
                    grid[row][col] = grid[row][col] + min(grid[row-1][col], grid[row][col-1])
                elif col:
                    grid[row][col] = grid[row][col] + grid[row][col-1]
                elif row:
                    grid[row][col] = grid[row][col] + grid[row-1][col]

        return grid[-1][-1]