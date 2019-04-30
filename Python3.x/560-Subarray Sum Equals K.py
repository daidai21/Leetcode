# Runtime: 56 ms, faster than 92.95% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Subarray Sum Equals K.
class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        count = add = 0
        dict = {0: 1}
        for i, item in enumerate(nums):
            add += item
            if dict.get(add - k, 0): count += dict.get(add - k)
            dict[add] = dict[add] + 1 if add in dict else 1
        return count


'''
使用map存储之前遍历的add值
'''


# Time Limit Exceeded
class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        count= 0
        for start in range(len(nums)):
            add = 0
            for end in range(start, len(nums)):
                add += nums[end]
                if add == k: count += 1
        return count


# storge sum
# Time Limit Exceeded
class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        count = 0
        add = [None] * (len(nums) + 1)
        add[0] = 0
        for i in range(1, len(nums) + 1):
            add[i] = add[i - 1] + nums[i - 1]
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if (add[end] - add[start]) == k: count += 1
        return count
