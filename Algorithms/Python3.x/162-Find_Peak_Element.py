# Runtime: 32 ms, faster than 94.17% of Python3 online submissions for Find Peak Element.
# Memory Usage: 13.3 MB, less than 33.43% of Python3 online submissions for Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_idx = 0
        for i, v in enumerate(nums):
            if v > nums[max_idx]: max_idx = i
        return max_idx
