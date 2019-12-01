# Runtime: 36 ms, faster than 92.77% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd_cnt = 0
        rows, cols = [0] * n, [0] * m
        for i, j in indices:
            rows[i] = rows[i] ^ 1
            cols[j] = cols[j] ^ 1
        for i in range(n):
            for j in range(m):
                odd_cnt += rows[i] ^ cols[j] == 1
        return odd_cnt
