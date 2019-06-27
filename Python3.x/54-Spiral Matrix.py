# Simulation
# Runtime: 36 ms, faster than 74.50% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.1 MB, less than 79.80% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        len_row, len_col = len(matrix), len(matrix[0])
        res = []
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]  # right, down, left, up
        r, c, di = 0, 0, 0
        for i in range(len_row * len_col):
            res.append(matrix[r][c])
            matrix[r][c] = None
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < len_row and 0 <= cc < len_col and matrix[cr][cc] is not None:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return res


# Runtime: 32 ms, faster than 90.38% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.1 MB, less than 63.77% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res