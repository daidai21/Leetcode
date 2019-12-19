# Runtime: 208 ms, faster than 85.97% of Python3 online submissions for Set Mismatch.
# Memory Usage: 14.7 MB, less than 11.11% of Python3 online submissions for Set Mismatch.
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]
