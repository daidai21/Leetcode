'''
# 没看懂
# space:1;time:n
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, max_len = 0, 0, 0
        for i in s:
            if i == '(': left += 1 
            else: right += 1
            if left == right: max_len = max(max_len, 2 * right)
            elif right >= left: left = right = 0
        left = right = 0
        for i in s[::-1]:
            if i == '(': left += 1
            else: right += 1
            if left == right: max_len = max(max_len, 2 * left)
            elif left >= right: left = right = 0
        return max_len
'''


# dp
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 2: return 0
        dp = [0 for _ in s]
        for i in range(1, length):
            print(dp)
            if s[i] == ')':
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] == '(':  # 匹配'()'
                    dp[i] = dp[i - 1] + 2
                    if j > 0:  # 这个是判断 left 前面是否能与后面继续连起来
                        dp[i] += dp[j - 1]
        return max(dp)


'''
1. dp[i]是存储的前i个子字符串的最长有效括号子串长度（这里是从0开始数）
2. 很明显dp[i]和dp[i-1]之间是有关系的：
    当s[i] == ‘(’时，dp[i]显然为0, 由于我们初始化dp的时候就全部设为0了，所以这种情况压根不用写
    当s[i] == ')'时， 如果在dp[i-1]的所表示的最长有效括号子串之前还有一个'('与s[i]对应，那么dp[i] = dp[i-1] + 2
        并且还可以继续往前追溯（如果前面还能连起来的话)
'''