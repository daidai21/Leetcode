# Runtime: 32 ms, faster than 99.61% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.1 MB, less than 83.28% of Python3 online submissions for String to Integer (atoi).
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0: return 0
        tmp, res, i = '0', 0, 0
        if str[0] in '+-': tmp, i = str[0], 1
        for s in str[i:]:
            if s.isdigit():
                tmp += s
            else:
                break
        if len(tmp) > 1:
            res = int(tmp)
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        else:
            return res
