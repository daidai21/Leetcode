# math
# Runtime: 868 ms, faster than 5.19% of Python3 online submissions for Largest Triangle Area.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Largest Triangle Area.
from itertools import permutations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # https://en.wikipedia.org/wiki/Shoelace_formula
        # Proof for a triangle
        triangle_area = lambda p1, p2, p3: 0.5 * (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - 
                                                  p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1])
        max_area = 0
        for three_points in permutations(points, 3):
            max_area = max(max_area, triangle_area(*three_points))
        return max_area
