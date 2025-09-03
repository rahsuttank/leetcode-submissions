class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    row[r].add(val)
                    col[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    box[box_index].add(val)

        def bt(index=0):
            if index == len(empties):
                return True
            r, c = empties[index]
            box_index = (r // 3) * 3 + (c // 3)
            for ch in map(str, range(1, 10)):
                if (ch not in row[r] and ch not in col[c]
                and ch not in box[box_index]):
                    board[r][c] = ch
                    row[r].add(ch)
                    col[c].add(ch)
                    box[box_index].add(ch)

                    if bt(index + 1):
                        return True

                    board[r][c] = '.'
                    row[r].remove(ch)
                    col[c].remove(ch)
                    box[box_index].remove(ch)
            return False

        bt()
        