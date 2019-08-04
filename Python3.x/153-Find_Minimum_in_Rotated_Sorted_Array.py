# Runtime: 48 ms, faster than 72.02% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 5.74% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


# Runtime: 48 ms, faster than 72.02% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.9 MB, less than 5.74% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            mid = int((l + r) / 2)
            if nums[mid] >= nums[l]:  # left continue
                l = mid + 1
            else:  # right continue
                r = mid
        return nums[l]
