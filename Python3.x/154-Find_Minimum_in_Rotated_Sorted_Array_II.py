# Runtime: 60 ms, faster than 85.44% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
# Memory Usage: 14.3 MB, less than 5.88% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


# Runtime: 52 ms, faster than 99.77% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
# Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[left]
