# BFS / DFS / Union-Find / Floyd

# Floyd
import collections  # 数据类型容器模块
import itertools  # 为高效循环而创建迭代器的函数
# Runtime: 36 ms, faster than 86.30% of Python3 online submissions for Evaluate Division.
# Memory Usage: 13.1 MB, less than 77.62% of Python3 online submissions for Evaluate Division.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = collections.defaultdict(dict)  # 建图
        for (num, den), val in zip(equations, values):  # 填图
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den], quot[den][num] = val, 1 / val
        for i, j, k in itertools.permutations(quot, 3):  # 填图
            if i in quot[j] and k in quot[i]:
                quot[j][k] = quot[j][i] * quot[i][k]
        return [quot[num].get(den, -1.0) for num, den in queries]  # 获取


# Union Find
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        parent = {}  # e.g. ["a", "b"] then parent[a] = b
        weight = {}  # e.g. a / b then weight[a] = 2.0
        ufind = UnionFind(parent, weight)
        for i, (x1, x2) in enumerate(equations):  # union
            if x1 not in parent and x2 not in parent:
                parent[x1], weight[x1] = x2, values[i]
                parent[x2], weight[x2] = x2, 1
            elif x1 not in parent:
                parent[x1], weight[x1] = x2, values[i]
            elif x2 not in parent:
                parent[x2], weight[x2] = x1, 1 / values[i]
            else:
                ufind.union(x1, x2, values[i])
        for x1, x2 in queries:  # find
            if x1 not in parent or x2 not in parent or ufind.find(x1) != ufind.find(x2):
                res.append(-1.0)
            else:
                factor1, factor2 = weight[x1], weight[x2]
                res.append(factor1 / factor2)
        return res


class UnionFind(object):
    def __init__(self, parent, weight):
        self.parent = parent
        self.weight = weight

    def find(self, vertex):  # 查找
        if self.parent[vertex] == vertex: return vertex
        root = self.find(self.parent[vertex])
        self.weight[vertex] *= self.weight[self.parent[vertex]]
        self.parent[vertex] = root
        return root

    def union(self, vertex1, vertex2, val):  # 联盟
        root1, root2 = self.find(vertex1), self.find(vertex2)
        self.parent[root1] = root2
        self.weight[root1] = self.weight[vertex2] * val / self.weight[vertex1]
