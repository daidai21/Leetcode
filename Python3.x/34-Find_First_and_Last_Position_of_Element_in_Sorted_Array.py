class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end, length = 0, len(nums) - 1, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target: break
            if nums[mid] < target: start = mid + 1
            else: end = mid - 1
        else: return [-1, -1]
        start = end = mid
        while start >= 0 and nums[start] == target: start -= 1
        while end <= length and nums[end] == target: end += 1
        return [start + 1, end - 1]


'''
先二分搜索找到目标值
然后向左和向右搜索
'''