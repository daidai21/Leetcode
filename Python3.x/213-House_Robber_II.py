# Runtime: 40 ms, faster than 47.61% of Python3 online submissions for House Robber II.
# Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for House Robber II.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))

    def dp(self, nums):
        cur, pre = 0, 0
        for num in nums:
            temp = max(num + pre, cur)
            pre = cur
            cur = temp
        return cur
