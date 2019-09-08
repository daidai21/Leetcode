# 排序
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums) / 2)]


'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checked, len_ = [], len(nums)
        for num in nums:
            if num not in checked and nums.count(num) > len_ / 2: return num
            checked.append(num)
'''
