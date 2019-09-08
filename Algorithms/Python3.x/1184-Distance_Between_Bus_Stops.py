# Brute Force
# Runtime: 60 ms, faster than 100.00% of Python3 online submissions for Distance Between Bus Stops.
# Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Distance Between Bus Stops.
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        return min(self.clockwise_distance(distance, start, destination, n),
                   self.anticlockwise_distance(distance, start, destination, n))

    def clockwise_distance(self, distance, start, destination, n):
        dis = 0
        while start != destination:
            if start == n - 1:
                start = 0
            else:
                start += 1
            dis += distance[start - 1]
        return dis

    def anticlockwise_distance(self, distance, start, destination, n):
        dis = 0
        while start != destination:
            if start == 0:
                start = n - 1
            else:
                start -= 1
            dis += distance[start]
        return dis


# Runtime: 56 ms, faster than 100.00% of Python3 online submissions for Distance Between Bus Stops.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Distance Between Bus Stops.
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        return distance[0] if len(distance) == 1 else min(sum(distance[start:destination]), 
                                                          sum(distance[:start]) + sum(distance[destination:]))
