# Runtime: 68 ms, faster than 26.91% of Python3 online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 14.1 MB, less than 6.08% of Python3 online submissions for Search in Rotated Sorted Array II.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False


# binary search
# Runtime: 68 ms, faster than 26.91% of Python3 online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 14 MB, less than 6.08% of Python3 online submissions for Search in Rotated Sorted Array II.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if target == nums[mid]:
                return True
            if nums[l] == nums[mid]:
                l += 1
            elif nums[l] > nums[mid]:  # right continue
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # left continue
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
