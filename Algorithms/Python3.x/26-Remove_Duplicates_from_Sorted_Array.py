# Runtime: 52 ms, faster than 98.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.8 MB, less than 45.41% of Python3 online submissions for Remove Duplicates from Sorted Array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        for num in nums[1:]:
            if num != nums[i]: nums[i + 1], i = num, i + 1
        return i + 1


# 双指针
