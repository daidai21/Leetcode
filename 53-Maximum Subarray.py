# dp
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = -9999999999
        for n in nums:
            i = max(n, n + i)
            j = max(i, j)
        return j


'''
随着遍历这个数组，在到每一个位置的时候，
弄一个局部最大L值，代表以当前位置为结尾的最大子串，
比如说我遍历到第i个，那么以第i个为结尾的最大子串就是我们要求的L。
'''
