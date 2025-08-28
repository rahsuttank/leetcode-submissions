class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        dirA = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                key = r - c
                dirA[key].append(grid[r][c])

        for key in dirA.keys():
            if key < 0:
                dirA[key] = sorted(dirA[key], reverse = True)
            else:
                dirA[key] = sorted(dirA[key])
        
        # print(dirA)

        for r in range(rows):
            for c in range(cols):
                key = r - c
                grid[r][c] = dirA[key].pop()
        
        return grid