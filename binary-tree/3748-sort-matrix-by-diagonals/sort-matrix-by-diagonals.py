class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        dirA = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                key = r - c
                if key < 0:
                    heapq.heappush(dirA[key], (grid[r][c]))
                else:
                    heapq.heappush(dirA[key], (-grid[r][c]))

        for r in range(rows):
            for c in range(cols):
                key = r - c
                if key < 0:
                    grid[r][c] = heapq.heappop(dirA[key])
                else:
                    grid[r][c] = -heapq.heappop(dirA[key])
        
        return grid