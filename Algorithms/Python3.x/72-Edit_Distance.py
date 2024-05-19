# dp
class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m, n = len(word1), len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): table[i][0] = i
        for j in range(n + 1): table[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]: table[i][j] = table[i - 1][j - 1]
                else: table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]


'''
分两种情况：
    1. word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
    2. word1[i]到word2[j]的最小改动就是替换、插入、删除都是dp[i - 1][j - 1] + 1，求最小即可
'''
class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m, n = len(word1), len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): 
            table[i][0] = i
        for j in range(n + 1): 
            table[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]: 
                    table[i][j] = table[i - 1][j - 1]
                else: 
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]

