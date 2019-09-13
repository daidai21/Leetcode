# brute force
# Runtime: 100 ms, faster than 25.68% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.7 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted([a for a in A if a & 1 == 0]) +\
               sorted([a for a in A if a & 1 == 1])


# Runtime: 96 ms, faster than 56.75% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.3 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            while l < r and A[l] % 2 == 0:
                l += 1
            while l < r and A[r] % 2 == 1:
                r -= 1
            A[l], A[r] = A[r], A[l]
            l, r = l + 1, r - 1
        return A
