# Runtime: 76 ms, faster than 62.01% of Python3 online submissions for The Skyline Problem.
# Memory Usage: 17.6 MB, less than 48.33% of Python3 online submissions for The Skyline Problem.
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(left, -high, right) for left, right, high in buildings] + 
                        list({(right, 0, None) for _, right, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x,  neg_high, right in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if neg_high:
                heapq.heappush(hp, (neg_high, right))
            if res[-1][1] + hp[0][0]:
                res.append([x, -hp[0][0]])
        return res[1:]
