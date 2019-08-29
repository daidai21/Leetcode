# Runtime: 264 ms, faster than 63.51% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15.6 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([a ** 2 for a in A])


# Runtime: 280 ms, faster than 33.71% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15.8 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        res = []
        while l <= r:
            if abs(A[l]) < abs(A[r]):
                res.append(A[r] ** 2)
                r -= 1
            else:
                res.append(A[l] ** 2)
                l += 1
        return res[::-1]
