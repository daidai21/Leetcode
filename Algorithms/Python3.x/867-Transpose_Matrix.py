# Runtime: 68 ms, faster than 93.54% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Transpose Matrix.
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(A[0])):
            new_row = []
            for j in range(len(A)):
                new_row.append(A[j][i])
            res.append(new_row)
        return res


# Runtime: 68 ms, faster than 93.54% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Transpose Matrix.
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))
