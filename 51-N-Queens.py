# 回溯
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.col = set()
        self.left = set()
        self.right = set()
        self.dfs(n, 0, [])
        return self.result

    def dfs(self, n, row, curstate):
        if row >= n: return self.result.append(curstate)  # 皇后填充完毕
        for col in range(n):
            if col in self.col or ((row + col) in self.left) or ((row - col) in self.right):  # 砍树枝
                continue
            self.col.add(col)
            self.left.add(col + row)
            self.right.add(row - col)
            self.dfs(n, row + 1, curstate + ['.'*col+'Q'+'.'*(n-col-1)])  # 逐行绘制
            self.col.remove(col)
            self.left.remove(col + row)
            self.right.remove(row - col)


'''

'''