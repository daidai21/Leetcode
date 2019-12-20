# Runtime: 24 ms, faster than 94.46% of Python3 online submissions for Rotate String.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotate String.
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        for i in range(len(A) + 1):
            if A == B[i:] + B[:i]:
                return True
        return False


# Runtime: 24 ms, faster than 94.46% of Python3 online submissions for Rotate String.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotate String.
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and A in B + B


# Time: O(n)
# Runtime: 24 ms, faster than 94.46% of Python3 online submissions for Rotate String.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Rotate String.
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        i, j, n = 0, 0, len(A)
        while i < n:
            if A[i] == B[j]:
                i, j = i + 1, j + 1
            else:
                if j:
                    j = 0
                else:
                    i += 1
        i = 0
        while j < n:
            if A[i] != B[j]:
                return False
            i, j = i + 1, j + 1
        return True
