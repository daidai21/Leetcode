'''
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
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum(x == '1' for x in bin(x ^ y))


'''
^:按位异或运算符：当两对应的二进位相异时，结果为1
'''