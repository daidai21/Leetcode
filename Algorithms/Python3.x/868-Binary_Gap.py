# Runtime: 32 ms, faster than 23.19% of Python3 online submissions for Binary Gap.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Gap.
class Solution:
    def binaryGap(self, N: int) -> int:
        lst = list(bin(N)[2:])
        if lst.count('1') < 2:
            return 0
        res = 0
        pre = lst.index('1')
        for idx in range(pre + 1, len(lst)):
            if lst[idx] == '1':
                res = max(res, idx - pre)
                pre = idx
        return res
