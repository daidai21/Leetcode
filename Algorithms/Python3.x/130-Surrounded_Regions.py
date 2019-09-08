# Runtime: 116 ms, faster than 93.61% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 14.4 MB, less than 61.48% of Python3 online submissions for Surrounded Regions.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return 
        len_row, len_col = len(board), len(board[0])
        save = [row_col 
                for k in range(len_row + len_col)
                for row_col in [(0, k), (len_row - 1, k), (k, 0), (k, len_col - 1)]]
        while save:
            row, col = save.pop()
            if 0 <= row < len_row and 0 <= col < len_col and board[row][col] == 'O':
                board[row][col] = 'S'
                save += [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
        board[:] = [["XO"[c == 'S'] for c in line]
                    for line in board]