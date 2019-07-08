# Runtime: 32 ms, faster than 97.14% of Python3 online submissions for Game of Life.
# Memory Usage: 13.3 MB, less than 22.55% of Python3 online submissions for Game of Life.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        len_row, len_col = len(board), len(board[0])
        res = [[0] * len_col for _ in range(len_row)]
        for row in range(len_row):
            for col in range(len_col):
                res[row][col] = self.judge(board, row, col, len_row, len_col)
        for row in range(len_row):
            for col in range(len_col):
                board[row][col] = res[row][col]

    def judge(self, board, row, col, len_row, len_col):
        same_neighbors, no_same_neighbors = 0, 0
        if row - 1 >= 0:
            if board[row][col] == board[row - 1][col]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if row - 1 >= 0 and col + 1 < len_col:
            if board[row][col] == board[row - 1][col + 1]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if col + 1 < len_col:
            if board[row][col] == board[row][col + 1]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if row + 1 < len_row and col + 1 < len_col:
            if board[row][col] == board[row + 1][col + 1]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if row + 1 < len_row:
            if board[row][col] == board[row + 1][col]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if row + 1 < len_row and col - 1 >= 0:
            if board[row][col] == board[row + 1][col - 1]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if col - 1 >= 0:
            if board[row][col] == board[row][col - 1]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        if col - 1 >= 0 and row - 1 >= 0:
            if board[row][col] == board[row - 1][col - 1]:
                same_neighbors += 1
            else:
                no_same_neighbors += 1
        # judge
        if board[row][col] == 1:
            if same_neighbors < 2:
                return 0
            elif same_neighbors <= 3:
                return 1
            else:
                return 0
        else:
            if no_same_neighbors == 3:
                return 1
            else:
                return 0