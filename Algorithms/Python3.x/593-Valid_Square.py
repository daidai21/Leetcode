# Runtime: 28 ms, faster than 94.11% of Python3 online submissions for Valid Square.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Square.
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        func_dis = lambda p, q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        distances = set([func_dis(p1, p2), func_dis(p1, p3), func_dis(p1, p4), func_dis(p2, p3), func_dis(p2, p4), func_dis(p3, p4)])
        return 0 not in distances and len(distances) == 2
