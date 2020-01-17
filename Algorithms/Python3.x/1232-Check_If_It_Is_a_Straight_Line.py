from typing import List


################################################################################
# Error: division by zero
################################################################################
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        # solve system of binary linear equations
        a = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        b = coordinates[0][1] - coordinates[0][0] * a
        # judge other point
        for coordinate in coordinates[2:]:
            if coordinate[0] * a + b != coordinate[1]:
                return False
        return True


# Runtime: 64 ms, faster than 41.16% of Python3 online submissions for Check If It Is a Straight Line.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Check If It Is a Straight Line.
################################################################################
################################################################################
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates[2:]:
            if (y - y1) * (x0 - x1) != (x - x1) * (y0 - y1):
                return False
        return True


print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  # true
print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))  # false
print(Solution().checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))  # true
print(Solution().checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))  # false
