# Runtime: 148 ms, faster than 56.35% of Python3 online submissions for Snakes and Ladders.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Snakes and Ladders.
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        need = {1: 0}
        bfs = [1]
        n = len(board)
        for x in bfs:
            for i in range(x + 1, x + 7):
                row, col = self.calc_idx(i, n)
                if board[row][col] > 0:
                    i = board[row][col]
                if i == n ** 2:
                    return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1

    def calc_idx(self, num, n):
        # calculate index according to normal matrix
        row = (num - 1) // n
        col = (num - 1) % n
        # exchange
        col = n - 1 - col if row % 2 == 1 else col  # column
        row = n - 1 - row  # row
        return row, col
