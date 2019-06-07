# Runtime: 328 ms, faster than 44.59% of Python3 online submissions for 4Sum II.
# Memory Usage: 34 MB, less than 86.63% of Python3 online submissions for 4Sum II.
class Solution:
    def fourSumCount(self, A, B, C, D):
        ab = {}
        for i in A:
            for j in B:
                ab[i + j] = ab.get(i+j, 0) + 1
        res = 0
        for i in C:
            for j in D:
                res += ab.get(-i - j, 0)       
        return res
