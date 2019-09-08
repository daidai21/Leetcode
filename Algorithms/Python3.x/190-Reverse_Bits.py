class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{0:032b}'.format(n)[::-1], 2)