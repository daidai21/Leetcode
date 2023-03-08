# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) <= 1:
            return s

        mp = {}
        for c in s:
            mp[c] = (mp[c] if c in mp else 0) + 1
        s = sorted(s, key=lambda k: (mp[k], k))
        n = len(s) // 2
        print(s, n, mp)
        if s[n - 1] == s[-1]:
            # 有字符串重复半数以上
            return ""
        
        l = s[:n]
        r = s[n:]
        print(l, r)
        for i in range(len(l)):
            s[2 * i + 1] = l[i]
        for i in range(len(r)):
            s[2 * i] = r[i]
        
        return "".join(s)

