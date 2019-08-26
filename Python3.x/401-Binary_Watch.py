# Runtime: 16 ms, faster than 89.34% of Python online submissions for Binary Watch.
# Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Binary Watch.
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["{0:d}:{1:02d}".format(h, m)
                for h in range(12)
                for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]
