# Runtime: 32 ms, faster than 98.04% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.2 MB, less than 67.21% of Python3 online submissions for Longest Common Prefix.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0: return ""
        min_len = min(len(s) for s in strs)
        res = ""
        cont = True
        for i in range(min_len):
            tmp = strs[0][i]
            same = True
            for s in strs[1:]:
                if s[i] != tmp:
                    same, cont = False, False
                    break
            if same and cont:
                res += tmp
        return res
