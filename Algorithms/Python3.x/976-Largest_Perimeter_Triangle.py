from typing import List


# Runtime: 196 ms, faster than 97.15% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 13.9 MB, less than 87.50% of Python3 online submissions for Largest Perimeter Triangle.
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return sum(A[i:i + 3])
        return 0


print(Solution().largestPerimeter([2,1,2]))  # 5
print(Solution().largestPerimeter([1,2,1]))  # 0
print(Solution().largestPerimeter([3,2,3,4]))  # 10
print(Solution().largestPerimeter([3,6,2,3]))  # 8
