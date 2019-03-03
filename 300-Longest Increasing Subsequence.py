# dp
class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2: return len(nums)
        dp = [1] * (len(nums) + 1)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
