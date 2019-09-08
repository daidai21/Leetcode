# Runtime: 112 ms, faster than 31.10% of Python3 online submissions for Shortest Path with Alternating Colors.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Shortest Path with Alternating Colors.
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        G = [[[], []] for _ in range(n)]
        for i, j in red_edges:
            G[i][0].append(j)
        for i, j in blue_edges:
            G[i][1].append(j)
        res = [[0, 0]] + [[float("inf"), float("inf")] for i in range(n - 1)]
        bfs = [[0, 0], [0, 1]]
        for i, color in bfs:  # i is index of node start
            for j in G[i][color]:  # j is endpoint of edge
                if res[j][color] == float("inf"):
                    res[j][color] = res[i][1 - color] + 1
                    bfs.append([j, 1 - color])
        return [x if x != float("inf") else -1 for x in map(min, res)]
