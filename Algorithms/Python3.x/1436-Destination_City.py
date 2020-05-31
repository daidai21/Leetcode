# Runtime: 56 ms, faster than 67.24% of Python3 online submissions for Destination City.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Destination City.
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = [], []
        for path in paths:
            start.append(path[0])
            end.append(path[1])
        for node in end:
            if node not in start:
                return node
