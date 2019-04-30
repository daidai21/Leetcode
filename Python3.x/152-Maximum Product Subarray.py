# dp
class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0: return 0
        min_tmp, max_tmp, result = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            min_, max_ = nums[i] * min_tmp, nums[i] * max_tmp
            max_tmp = max(min_, max_, nums[i])
            min_tmp = min(min_, max_, nums[i])
            result = max(result, max_tmp)
        return result


'''
之前的最小值（就是负值） * 当前的值（为负） == 当前最大
之前的最大值（就是正值） * 当前的值（为正） == 当前最大
'''
