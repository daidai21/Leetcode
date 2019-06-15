class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([col for row in matrix for col in row])[k - 1]


# Runtime: 48 ms, faster than 96.13% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 17.1 MB, less than 93.92% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:  # 在row插入mid的位置
                low = mid + 1
            else:
                high = mid
        return low
