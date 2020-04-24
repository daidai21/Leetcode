# Runtime: 172 ms, faster than 20.92% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.2 MB, less than 64.52% of Python3 online submissions for K-diff Pairs in an Array.
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 1
        res = 0
        while right < len(nums):
            if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right += 1
            elif nums[left] + k == nums[right]:
                res += 1
                left += 1
                right += 1
            elif nums[left] + k > nums[right]:
                right += 1
            else:
                left += 1
            right = max(left + 1, right)
        return res
