# backtracking
# Runtime: 828 ms, faster than 19.47% of Python3 online submissions for Sudoku Solver.
# Memory Usage: 14.6 MB, less than 10.71% of Python3 online submissions for Sudoku Solver.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solver()

    def find_unassigned(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == '.':
                    print(row, col)
                    return row, col
        return -1, -1

    def solver(self):
        row, col = self.find_unassigned()
        if row == -1 and col == -1:
            return True
        for ch in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.is_valid(row, col, ch):
                self.board[row][col] = ch
                if self.solver():
                    return True
                else:
                    self.board[row][col] = '.'
        return False

    def is_valid(self, row, col, ch):
        for idx in range(len(self.board)):
            if ch == self.board[idx][col]:  # check row
                return False
            if ch == self.board[row][idx]:  # check col
                return False
        for idx_row in range(3):  # check square
            for idx_col in range(3):
                if ch == self.board[row - row % 3 + idx_row][col - col % 3 + idx_col]:
                    return False
        return True
