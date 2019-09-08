class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n, res = len(M), 0
        def dfs(curr, n):
            for i in range(n):
                if M[curr][i] == 1:
                    M[curr][i] = M[i][curr] = 0
                    dfs(i, n)

        for i in range(n):
            if M[i][i] == 1:
                res += 1
                dfs(i, n)
        return res


# UnionFind set
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        circles = {x: x for x in range(n)}
        def find(node):
            if circles[node] == node:
                return node
            root = find(circles[node])
            circles[node] = root
            return root

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)
        return sum([k == v for k, v in circles.items()])
