class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dis = 0
        for i in bin(x ^ y):
            if i == '1': dis += 1
        return dis


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum(x == '1' for x in bin(x ^ y))


# Runtime: 24 ms, faster than 99.64% of Python3 online submissions for Hamming Distance.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Hamming Distance.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
