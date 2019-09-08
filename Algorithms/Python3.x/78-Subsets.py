# dfs
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


# 迭代
class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        result = [[]]
        for num in sorted(nums):
            result += [item + [num] for item in result]
        return result
