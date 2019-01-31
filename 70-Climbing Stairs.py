'''
# dp
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        tmp = [1, 2]
        for i in range(2, n): tmp.append(tmp[i - 1] + tmp[i - 2])
        return tmp[n - 1]
'''


# dp优化
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        i, j = 1, 2
        for n in range(2, n): i, j = j, i + j
        return j
