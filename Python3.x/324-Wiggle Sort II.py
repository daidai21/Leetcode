# Runtime: 116 ms, faster than 82.87% of Python3 online submissions for Wiggle Sort II.
# Memory Usage: 14.3 MB, less than 46.00% of Python3 online submissions for Wiggle Sort II.
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(sorted(nums)[::-1]):
            nums[(1 + 2 * i) % (len(nums) | 1)] = num


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(sorted(nums)[::-1]):
            nums[(1 + 2 * i) % (len(nums) if len(nums) % 2 == 1 else len(nums) + 1)] = num
