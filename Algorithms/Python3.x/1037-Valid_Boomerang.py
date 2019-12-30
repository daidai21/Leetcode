# calcuate slope
# Runtime: 32 ms, faster than 73.11% of Python3 online submissions for Valid Boomerang.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Boomerang.
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) != \
               (points[0][0] - points[2][0]) * (points[0][1] - points[1][1])
