# Runtime: 360 ms, faster than 47.17% of Python3 online submissions for Add to Array-Form of Integer.
# Memory Usage: 14.4 MB, less than 5.00% of Python3 online submissions for Add to Array-Form of Integer.
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i:
                A[i - 1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A
