# union-find
# Runtime: 68 ms, faster than 59.57% of Python3 online submissions for Redundant Connection.
# Memory Usage: 14.2 MB, less than 14.29% of Python3 online submissions for Redundant Connection.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.root = [-1] * (len(edges) + 1)
        for edge in edges:
            x = self.find(edge[0])
            y = self.find(edge[1])
            if x == y:
                return edge
            self.root[x] = y
        return [-1, -1]

    def find(self, x):
        while self.root[x] != -1:
            x = self.root[x]
        return x
