# 冒泡
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        if nums == []: return None
        for j in range(k):
            max_item = j
            for i in range(j, len(nums)):
                if nums[i] is not None and nums[i] > nums[max_item]: max_item = i
            nums[max_item], nums[j] = nums[j], nums[max_item]
        return nums[k - 1]


# 维护一个优先队列
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        if len(nums) == 0: return None
        max_list = nums[:k]
        for n in range(k, len(nums)):
            if nums[n] > max_list[0]:
                max_list[0] = nums[n]
                max_list.sort()
        # print(max_list)
        max_list.sort()
        return max_list[0]


# 暴力
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums.sort()
        return nums[-k]


# 暴力的优化
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        return sorted(nums)[-k]


class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        if nums == []: return None
        for j in range(k):
            max_item = j
            for i in range(j, len(nums)):
                if nums[i] is not None and nums[i] > nums[max_item]: max_item = i
            nums[max_item], nums[j] = nums[j], nums[max_item]
        return nums[k - 1]
