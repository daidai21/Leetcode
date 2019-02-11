# 单调队列
# time: 92 ms, faster than 100.00%
# space: 14.4 MB, less than 78.34%
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        reuslt, last_max_index = [], -1
        for i in range(len(nums) - k + 1):
            if last_max_index < i:
                last_max_index = i
                for j in range(i, i + k):
                    if nums[j] > nums[last_max_index]: last_max_index = j
            elif nums[last_max_index] < nums[i + k - 1]: last_max_index = i + k - 1
            reuslt.append(nums[last_max_index])
        return reuslt


# 常规思路
# time: 536 ms, faster than 20.90%
# space: 14.4 MB, less than 75.91%
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums or k == 0: return []
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]
