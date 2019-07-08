# Runtime: 16 ms, faster than 95.57% of Python online submissions for Remove Element.
# Memory Usage: 11.9 MB, less than 13.53% of Python online submissions for Remove Element.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j, _ in enumerate(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
