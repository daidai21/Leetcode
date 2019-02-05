# 贪心
class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        farest = nums[0]
        for i in range(len(nums)):
            if i <= farest and nums[i] + i > farest:
                farest = nums[i] + i
            if farest >= len(nums) - 1: return True
        return False
