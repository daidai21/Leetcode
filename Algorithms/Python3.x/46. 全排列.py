# https://leetcode.cn/problems/permutations/description/

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.dfs(0)
        return self.res

    def dfs(self, i):
        if len(self.nums) - 1 == i:
            self.res.append(list(self.nums))
            return
        for j in range (i, len(self.nums)):
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.dfs(i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

