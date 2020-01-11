# Runtime: 168 ms, faster than 61.92% of Python3 online submissions for Matrix Cells in Distance Order.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Matrix Cells in Distance Order.
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[row, col] for row in range(R) for col in range(C)]
        res.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return res
