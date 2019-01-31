'''
# 列表
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        for num in nums:
            if num in tmp: tmp.remove(num)
            else: tmp.append(num)
        return tmp[0]
'''


# math
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


'''
2 * (a + b + c) - (a + a + b + b +c) = c  # 其中c是奇数个，a和b是偶数个
'''
