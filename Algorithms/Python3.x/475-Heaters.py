# Time Limit Exceeded
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        for house in houses:
            tmp_radius = float("inf")
            for heater in heaters:
                tmp_radius = min(tmp_radius, abs(house - heater))
            radius = max(radius, tmp_radius)
        return radius


# binary search
# Runtime: 292 ms, faster than 99.63% of Python3 online submissions for Heaters.
# Memory Usage: 16.1 MB, less than 16.67% of Python3 online submissions for Heaters.
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        idx = 0
        length = len(heaters)
        for house in houses:
            while idx < length - 1 and heaters[idx] + heaters[idx + 1] <= 2 * house:
                idx += 1
            radius = max(radius, abs(house - heaters[idx]))
        return radius
