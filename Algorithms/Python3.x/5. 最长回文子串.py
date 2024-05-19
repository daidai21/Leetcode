# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/description/

"""
给你一个字符串 s，找到 s 中最长的 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s, self.ln = s, len(s)
        if self.ln == 0:
            return s
        self.res, self.mx = s[0], 1
        for i in range(self.ln):
            self.helper(i, i + 1)
            self.helper(i, i)
        return self.res

    def helper(self, l, r):
        while l >= 0 and r < self.ln and self.s[l] == self.s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        if r - l + 1 > self.mx:
            self.res = self.s[l:r + 1]
            self.mx = r - l + 1
        return


