# Time Limit Exceeded
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) < 3:
            return 
        for i in range(1, len(A) - 1):
            if max(A[:i]) < A[i] and max(A[i + 1:]) < A[i]:
                return i


# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 15.1 MB, less than 6.06% of Python3 online submissions for Peak Index in a Mountain Array.
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A) - 1):
            if A[i] > A[i + 1]:
                return i


# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 15 MB, less than 6.06% of Python3 online submissions for Peak Index in a Mountain Array.
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 14.9 MB, less than 6.06% of Python3 online submissions for Peak Index in a Mountain Array.
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
