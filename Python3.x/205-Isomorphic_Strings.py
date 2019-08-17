# Runtime: 56 ms, faster than 27.40% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.1 MB, less than 17.50% of Python3 online submissions for Isomorphic Strings.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) < 2:
            return True
        return self.judge(s, t) and self.judge(t, s)

    def judge(self, s, t):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True
