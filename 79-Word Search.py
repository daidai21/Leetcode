# dfs
class Solution:
    def exist(self, board, word):
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j): return True  # 起点
        return False

    def dfs(self, board, word, i, j):  # 从i，j为开始检查是否能找到单词
        if len(word) == 0: return True  # 所有单词检查完毕
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # 第一个字符已经被检查
        board[i][j] = '#'  # 标记已经检查过的的字符，避免重复检查
        res = self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i - 1, j) or \
            self.dfs(board, word[1:], i, j + 1) or self.dfs(board, word[1:], i, j - 1)  # 检查是否能沿着一个方向匹配
        board[i][j] = tmp
        return res
