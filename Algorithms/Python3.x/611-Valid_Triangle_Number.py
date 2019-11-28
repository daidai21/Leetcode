# Time Limit Exceeded
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        count += 1
        return count
