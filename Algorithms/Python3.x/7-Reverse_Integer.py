# 暴力
# Runtime: 36 ms, faster than 92.74% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.2 MB, less than 74.27% of Python3 online submissions for Reverse Integer.
class Solution:
    def reverse(self, x: int) -> int:
        tmp = str(x)
        if tmp[0] == '-':
            result = int(tmp[0] + tmp[1:][::-1])
            if result > 2 ** 31 or result < -2 ** 31:
                return 0
            else:
                return result
        else:
            result = int(tmp[::-1])
            if result > 2 ** 31 or result < -2 ** 31:
                return 0
            else:
                return result


# 精简后
# Runtime: 28 ms, faster than 99.54% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.3 MB, less than 53.02% of Python3 online submissions for Reverse Integer.
class Solution:
    def reverse(self, x: int) -> int:
        tmp = str(x)
        if tmp[0] == '-':
            result = int(tmp[0] + tmp[1:][::-1])
            return 0 if result > 2 ** 31 or result < -2 ** 31 else result
        else:
            result = int(tmp[::-1])
            return 0 if result > 2 ** 31 or result < -2 ** 31 else result


# Runtime: 36 ms, faster than 92.74% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.2 MB, less than 74.27% of Python3 online submissions for Reverse Integer.
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(abs(x))[::-1]) if x > 0 else -int(str(abs(x))[::-1])
        return res if -2 ** 31 - 1 < res < 2 ** 31 else 0
