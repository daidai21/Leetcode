# 暴力
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums.sort()
        return nums[-k]


# 暴力的优化
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        return sorted(nums)[-k]
