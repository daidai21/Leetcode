# Runtime: 68 ms, faster than 79.77% of Python3 online submissions for Triangle.
# Memory Usage: 14.7 MB, less than 13.51% of Python3 online submissions for Triangle.
# buttom -> up, O(n) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return None
        temp = triangle[-1]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                temp[col] = min(temp[col], temp[col + 1]) + triangle[row][col]
        return temp[0]
