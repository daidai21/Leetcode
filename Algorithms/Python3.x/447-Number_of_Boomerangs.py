# Runtime: 1396 ms, faster than 33.13% of Python3 online submissions for Number of Boomerangs.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Number of Boomerangs.
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for point1 in points:
            distances = {}
            for point2 in points:
                distance = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
                distances[distance] = distances.get(distance, 0) + 1
            for distance, _ in distances.items():
                result += distances.get(distance, 0) * (distances.get(distance, 0) - 1)
        return result
