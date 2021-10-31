# 896. 单调数列

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0  # 1为增长，-1为减少
        for i in range(1, len(nums)):
            if direction == 0:
                if nums[i - 1] < nums[i]:
                    direction = 1
                elif nums[i - 1] > nums[i]:
                    direction = -1
            elif direction == 1:
                if nums[i - 1] > nums[i]:
                    return False
            elif direction == -1:
                if nums[i - 1] < nums[i]:
                    return False
        return True
