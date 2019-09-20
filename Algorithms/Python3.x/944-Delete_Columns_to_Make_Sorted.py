# Runtime: 100 ms, faster than 99.76% of Python3 online submissions for Delete Columns to Make Sorted.
# Memory Usage: 14.7 MB, less than 8.33% of Python3 online submissions for Delete Columns to Make Sorted.
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        len_row, len_col = len(A), len(A[0])
        S = ''.join(A)
        length = 0
        for col in range(len_col):
            length += S[col::len_col] != ''.join(sorted(S[col::len_col]))
        return length
