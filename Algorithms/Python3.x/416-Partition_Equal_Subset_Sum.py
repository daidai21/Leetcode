# dp
# Runtime: 680 ms, faster than 50.36% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 13.2 MB, less than 43.64% of Python3 online submissions for Partition Equal Subset Sum.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_half = sum(nums)
        if sum_half & 1: return False  # if sum is odd number return False
        else: sum_half = int(sum_half / 2)
        dp = [False] * (sum_half + 1)
        dp[0] = True
        for num in nums:
            for i in range(sum_half, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[sum_half]


# dictionary
# Runtime: 1116 ms, faster than 34.80% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 15.2 MB, less than 36.36% of Python3 online submissions for Partition Equal Subset Sum.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dict = {0}  # set
        for num in nums:
            dict.update({(tmp + num) for tmp in dict})
        return sum(nums) / 2.0 in dict
