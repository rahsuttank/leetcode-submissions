class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        ans = []
        dirA = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                dirA[r+c].append(mat[r][c])

        for i in range(rows + cols - 1):
            if i % 2 != 0:
                ans.extend(dirA[i])
            else:
                ans.extend(dirA[i][::-1])
        
        return ans