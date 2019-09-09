# Runtime: 224 ms, faster than 32.24% of Python3 online submissions for Minesweeper.
# Memory Usage: 16.4 MB, less than 20.00% of Python3 online submissions for Minesweeper.
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == "M":  # is thunder
                board[row][col] = "X"
            elif board[row][col] == 'E':
                n = 0
                for r, c in directions:
                    if 0 <= row + r < len(board) and 0 <= col + c < len(board[0]):
                        if board[row + r][col + c] == "M":
                            n += 1
                board[row][col] = str(n or 'B')  # fill thunder number
                if not n:
                    for r, c in directions:
                        self.updateBoard(board, [row + r, col + c])  # matrix recursion is reference (not copy)
        return board
