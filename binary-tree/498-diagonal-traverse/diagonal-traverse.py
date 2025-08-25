class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        ans = []
        
        for d in range(rows + cols - 1):
            temp = []
            # starting row for this diagonal
            r = 0 if d < cols else d - cols + 1
            # starting col for this diagonal
            c = d if d < cols else cols - 1

            # collect elements in this diagonal
            while r < rows and c >= 0:
                temp.append(mat[r][c])
                r += 1
                c -= 1
            
            # reverse on even diagonals
            if d % 2 == 0:
                ans.extend(temp[::-1])
            else:
                ans.extend(temp)
        
        return ans
