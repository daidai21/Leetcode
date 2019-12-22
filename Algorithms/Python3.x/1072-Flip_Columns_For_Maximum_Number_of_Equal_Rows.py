# Runtime: 2508 ms, faster than 5.15% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        result = 0
        flip = [0] * len(matrix[0])
        for i in range(len(matrix)):
            cnt = 0
            for j in range(len(matrix[0])):
                flip[j] = 1 - matrix[i][j]
            for k in range(len(matrix)):
                if matrix[k] == matrix[i] or matrix[k] == flip:
                    cnt += 1
            result = max(result, cnt)
        return result
