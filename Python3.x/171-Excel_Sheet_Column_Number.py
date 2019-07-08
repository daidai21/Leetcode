# Runtime: 40 ms, faster than 86.64% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.1 MB, less than 86.39% of Python3 online submissions for Excel Sheet Column Number.
class Solution:
    def titleToNumber(self, s: str) -> int:
        len_s, res = len(s), 0
        if len_s == 0: return 0
        for c in s:  # c是char在string中循环
            len_s -= 1
            res += (ord(c) - 64) * 26 ** len_s  # len_s记位
        return res
