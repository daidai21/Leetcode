# Runtime: 64 ms, faster than 71.86% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 14 MB, less than 5.16% of Python3 online submissions for Remove Duplicates from Sorted Array II.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i
