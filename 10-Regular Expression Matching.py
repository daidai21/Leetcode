# "."  匹配任意单个字符， "*"  匹配0个或者多个前面的元素


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]  # 这里使用table[i + 1][j + 1]表示s[0...i]和p[0...j]匹配的结果
        dp[0][0] = True  # s和p都为空时匹配
        for col in range(1, len(p) + 1):  # s为空串时
            if p[col - 1] == '*' and col >= 2: dp[0][col] = dp[0][col - 2]  # 只有x*能匹配空串，若有*，它的真值一定和dp[0][j-2]的相同
        for row in range(1, len(s) + 1):  # 行循环
            for col in range(1, len(p) + 1):  # 列循环
                if p[col - 1] == '*':  # 假设当前位置是dp[row][col]
                    dp[row][col] = dp[row][col - 2] or (dp[row - 1][col] and (p[col - 2] == s[row - 1] or p[col - 2] == '.'))
                else:  # 假设当前位置是dp[row][col]
                    dp[row][col] = (p[col - 1] == s[row - 1] or p[col - 1] == '.') and dp[row - 1][col - 1]
        return dp[-1][-1]


'''
每次s字符串往下走一个字符，和所有的p子串进行匹配，接下来分两种情况进行分类。

      ( a )  假设当前位置为dp[i][j]，若p[j-1] == "*"时，"*"的用法分为两种（1：代表空串  2：代表一个或者多个前一个字符）

要想dp[i][j] =1，需要满足下列条件中的任一个：

                    （a.1）dp[i][j-2] =1时，此时"*"代表空串

                    （a.2）dp[i-1][j] =1时且满足（p[j-2]==s[i-1] or p[j-2]=="."），此时"*"代表对前一字符的复制

      ( b )  若p[j-1]!= "*"时，要想dp[i][j] =1，需满足（p[j-1]==s[i-1] or p[j-1]=="."），且还要判断前面的是否匹配，即dp[i-1][j-1]的值是否为True。
'''