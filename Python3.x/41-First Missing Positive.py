# Runtime: 36 ms, faster than 83.01% of Python3 online submissions for First Missing Positive.
# Memory Usage: 13.1 MB, less than 65.86% of Python3 online submissions for First Missing Positive.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            print(nums)
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tmp - 1] = tmp
            else:
                i += 1
        for idx, val in enumerate(nums):
            if val != idx + 1:
                return idx + 1
        return n + 1
