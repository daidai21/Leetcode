# Runtime: 24 ms, faster than 6.63% of Python online submissions for Guess Number Higher or Lower.
# Memory Usage: 11.7 MB, less than 85.19% of Python online submissions for Guess Number Higher or Lower.
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            temp = guess(mid)
            if temp == 0:
                return mid
            elif temp == -1:
                r = mid - 1
            else:
                l = mid + 1
