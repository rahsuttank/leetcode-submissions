class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        # deq = deque()
        # dirs = [[1, 0], [0, 1]]
        # deq.append(mat[0][0])
        ans = []
        # while deq:
        dirA = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                dirA[r+c].append(mat[r][c])

        # print(dirA)

        for i in range(rows + cols - 1):
            if i % 2 != 0:
                ans.extend(dirA[i])
            else:
                ans.extend(dirA[i][::-1])
        
        return ans