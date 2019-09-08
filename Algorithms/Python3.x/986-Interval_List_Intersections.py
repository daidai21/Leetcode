# merge
# Runtime: 180 ms, faster than 30.41% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.3 MB, less than 6.06% of Python3 online submissions for Interval List Intersections.
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        a, b = 0, 0
        while a < len(A) and b < len(B):
            low = max(A[a][0], B[b][0])
            high = min(A[a][1], B[b][1])
            if low <= high:
                result.append([low, high])
            if A[a][1] < B[b][1]:  # 贪心  保留结尾大的区间才会和另外一个区间集相交，因此应该移动的指针是结尾区间小的那个。
                a += 1
            else:
                b += 1
        return result
