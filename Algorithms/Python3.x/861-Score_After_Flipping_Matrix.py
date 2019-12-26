# greedy
# Runtime: 28 ms, faster than 98.65% of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Score After Flipping Matrix.
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # flip each row
        for row in range(len(A)):
            if A[row][0] == 0:  # need flip
                for col in range(len(A[0])):
                    A[row][col] = 1 - A[row][col]
        # flip each column
        for col in range(len(A[0])):
            sum_one = 0
            for row in range(len(A)):
                sum_one += A[row][col]
            if sum_one * 2 < len(A):
                for row in range(len(A)):
                    A[row][col] = 1 - A[row][col]
        # calculate result
        res = 0
        for row in range(len(A)):
            num = 0
            for col in range(len(A[0])):
                num = num * 2 + A[row][col]
            res += num
        return res
