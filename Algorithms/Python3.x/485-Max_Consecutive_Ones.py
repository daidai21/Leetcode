# Runtime: 380 ms, faster than 98.79% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 0
        return max(ans, tmp)
