# 36ms
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([x in J for x in S])  # 会生成bool列表，然后求和


'''
# 暴力的优化 | 40ms
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        for j in J:
            n += S.count(j)
        return n
'''


'''
# 暴力 | 52ms
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        for j in J:
            for s in S:
                if j == s: n += 1
        return n
'''