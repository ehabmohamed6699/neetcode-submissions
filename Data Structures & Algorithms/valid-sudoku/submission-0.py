class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row = list(filter(lambda x: x != '.', row))
            if len(row) != len(set(row)):
                return False
        for i in range(9):
            col = [x[i] for x in board]
            col = list(filter(lambda x: x != '.', col))
            if len(col) != len(set(col)):
                return False
        for i in range(9):
            col_idxs = [3*(i % 3) + k for k in range(3)]
            row_idxs = [i - (i % 3) + k for k in range(3)]
            cells = [board[r][c] for c in col_idxs for r in row_idxs]
            cells = list(filter(lambda x: x != '.', cells))
            print(cells)
            if len(cells) != len(set(cells)):
                return False
        return True