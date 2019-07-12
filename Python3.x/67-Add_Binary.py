# Runtime: 36 ms, faster than 90.19% of Python3 online submissions for Add Binary.
# Memory Usage: 13.2 MB, less than 55.28% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# Runtime: 40 ms, faster than 70.45% of Python3 online submissions for Add Binary.
# Memory Usage: 13.1 MB, less than 86.02% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, flag = "", 0
        len_a, len_b = len(a) - 1, len(b) - 1
        while len_a >= 0 or len_b >= 0 or flag:
            cur_val = (len_a >= 0 and a[len_a] == '1') + (len_b >= 0 and b[len_b] == '1')
            flag, val = divmod(cur_val + flag, 2)
            res = str(val) + res
            len_a, len_b = len_a - 1, len_b - 1
        return res
