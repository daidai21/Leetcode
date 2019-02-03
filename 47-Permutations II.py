# 回溯
# time:276 ms  space:6.7 MB
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, cur, res):
            if not nums: res.add(cur)
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i + 1:], cur + (nums[i], ), res)

        res = set()
        dfs(nums, (), res)
        return list(res)
