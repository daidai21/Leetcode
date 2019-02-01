# 暴力 | 676 ms
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]: n += 1
        return n
