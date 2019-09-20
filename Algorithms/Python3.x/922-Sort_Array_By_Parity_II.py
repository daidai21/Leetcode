# Runtime: 228 ms, faster than 99.63% of Python3 online submissions for Sort Array By Parity II.
# Memory Usage: 15.9 MB, less than 8.70% of Python3 online submissions for Sort Array By Parity II.
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
