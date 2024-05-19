
# 53. 最大子数组和

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = nums[0]
        tmp = 0
        for num in nums:
            tmp = max(tmp + num, num)
            res = max(res, tmp)
        return res

