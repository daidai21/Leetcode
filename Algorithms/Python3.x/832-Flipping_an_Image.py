# Runtime: 56 ms, faster than 91.04% of Python3 online submissions for Flipping an Image.
# Memory Usage: 13.9 MB, less than 6.00% of Python3 online submissions for Flipping an Image.
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return A
        len_row, len_col = len(A), len(A[0])
        for i in range(len_row):
            for j in range(len_col // 2):
                A[i][j], A[i][len_col - j - 1] = A[i][len_col - j - 1], A[i][j]
        for i in range(len_row):
            for j in range(len_col):
                A[i][j] = (1, 0)[A[i][j]]
        return A
