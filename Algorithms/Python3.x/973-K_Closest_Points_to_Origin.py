# Time Limit Exceeded
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis, res = [], []
        for x, y in points:
            dis.append(x ** 2 + y ** 2)
        for _ in range(K):
            idx = dis.index(min(dis))
            res.append(points[idx])
            dis[idx] = float("inf")
        return res


# Time Limit Exceeded
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis, res = [], []
        for x, y in points:
            dis.append(x ** 2 + y ** 2)
        for _ in range(K):
            idx = 0
            for i in range(len(points)):
                if dis[idx] > dis[i]:
                    idx = i
            res.append(points[idx])
            dis[idx] = float("inf")
        return res


# Runtime: 748 ms, faster than 69.09% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.4 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]


# Runtime: 728 ms, faster than 85.74% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.3 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]
