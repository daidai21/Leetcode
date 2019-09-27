# Runtime: 28 ms, faster than 99.49% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for Available Captures for Rook.
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        eats = 0
        len_row, len_col = len(board), len(board[0])
        row, col = 0, 0
        for i in range(len_row):
            for j in range(len_col):
                if board[i][j] == 'R':
                    row, col = i, j
                    break
                    break
        # up
        i = row - 1
        while i >= 0 and board[i][col] != 'B':
            if board[i][col] == 'p':
                eats += 1
                break
            i -= 1
        # down
        i = row + 1
        while i < len_row and board[i][col] != 'B':
            if board[i][col] == 'p':
                eats += 1
                break
            i += 1
        # left
        j = col - 1
        while j >= 0 and board[row][j] != 'B':
            if board[row][j] == 'p':
                eats += 1
                break
            j -= 1
        # right
        j = col + 1
        while j < len_col and board[row][j] != 'B':
            if board[row][j] == 'p':
                eats += 1
                break
            j += 1
        # output
        return eats
