# 回溯
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        def backtrack(nums, tmp, arr):
            if len(arr) == len(nums): tmp.append(arr)
            else:
                for i in range(len(nums)):
                    if nums[i] not in arr: backtrack(nums, tmp, arr + [nums[i]])

        backtrack(nums, tmp, [])
        return tmp



class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        def backtrack(nums, tmp, arr):
            if len(arr) == len(nums): 
                tmp.append(arr)
            else:
                for i in range(len(nums)):
                    if nums[i] not in arr: 
                        backtrack(nums, tmp, arr + [nums[i]])

        backtrack(nums, tmp, [])
        return tmp

