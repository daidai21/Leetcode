# Runtime: 216 ms, faster than 83.28% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.2 MB, less than 6.67% of Python3 online submissions for Non-decreasing Array.
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                else:
                    p = i
        return p is None or p == 0 or p == len(nums) - 2 or nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2]
