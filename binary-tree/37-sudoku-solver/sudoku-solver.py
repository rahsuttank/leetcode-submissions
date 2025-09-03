class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)

        # Step 1: Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])

        # Step 2: Backtracking function
        def backtrack(r, c):
            # If we reach the end of the row, move to next
            if c == 9:
                return backtrack(r + 1, 0)
            
            # If we reach the end of the board, solved
            if r == 9:
                return True

            # If cell is already filled, skip
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            # Try digits 1–9
            for i in map(str, range(1, 10)):
                if i not in rows[r] and i not in cols[c] and i not in squares[(r//3, c//3)]:
                    # Place the number
                    board[r][c] = i
                    rows[r].add(i)
                    cols[c].add(i)
                    squares[(r//3, c//3)].add(i)

                    # Recurse
                    if backtrack(r, c + 1):
                        return True

                    # Undo move (backtrack)
                    board[r][c] = "."
                    rows[r].remove(i)
                    cols[c].remove(i)
                    squares[(r//3, c//3)].remove(i)

            # No valid number, trigger backtracking
            return False

        backtrack(0, 0)
