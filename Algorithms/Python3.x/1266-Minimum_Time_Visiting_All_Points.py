class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        x1, y1 = points[0]
        for x2, y2 in points[1:]:
            result += max(abs(x1 - x2), abs(y1 - y2))
            x1, y1 = x2, y2
        return result
