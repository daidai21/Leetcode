# 常规思路堆逻辑
# Runtime: 48 ms, faster than 88.39% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.3 MB, less than 36.37% of Python3 online submissions for Valid Sudoku.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.check_row(board) and self.check_col(board) and self.check_array(board):
            return True
        else:
            return False

    def check_row(self, board):
        for i in range(9):
            row = ""
            for j in range(9):
                if board[i][j] not in row:
                    row += board[i][j]
                elif board[i][j] != '.':
                    return False
        return True

    def check_col(self, board):
        for i in range(9):
            col = ""
            for j in range(9):
                if board[j][i] not in col:
                    col += board[j][i]
                elif board[j][i] != '.':
                    return False
        return True

    def check_array(self, board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                arr = ""
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] not in arr:
                            arr += board[i][j]
                        elif board[i][j] != '.':
                            return False
        return True


# set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if (i, board[i][j]) in tmp or (board[i][j], j) in tmp or (i // 3, j // 3, board[i][j]) in tmp:
                        return False
                    tmp.add((i, board[i][j]))
                    tmp.add((board[i][j], j))
                    tmp.add((i // 3, j // 3, board[i][j]))
        return True
