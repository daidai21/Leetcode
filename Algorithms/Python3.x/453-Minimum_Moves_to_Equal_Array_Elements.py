# Time Limit Exceeded
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        while len(set(nums)) != 1:
            max_val_idx = nums.index(max(nums))
            for i in range(len(nums)):
                if max_val_idx != i:
                    nums[i] += 1
            ans += 1
        return ans


# math
# Runtime: 272 ms, faster than 98.75% of Python3 online submissions for Minimum Moves to Equal Array Elements.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Minimum Moves to Equal Array Elements.
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
