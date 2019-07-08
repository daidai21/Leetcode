# 暴力
# 先排序再遍历搜索
# Runtime: 48 ms, faster than 61.14% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 16.4 MB, less than 90.16% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]: return True
        return False


# set
# Runtime: 40 ms, faster than 95.12% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19 MB, less than 39.66% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(list(set(nums))) == len(nums) else True


# Time Limit Exceeded
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                if nums[i] == nums[j]: return True
        return False
