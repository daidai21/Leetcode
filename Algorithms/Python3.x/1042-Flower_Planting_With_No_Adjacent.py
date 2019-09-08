class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [1] * N
        mem = [[] for _ in range(N)]
        for x, y in paths:
            mem[x - 1].append(y - 1)
            mem[y - 1].append(x - 1)
        for i in range(1, N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in mem[i]}).pop()
        return res
