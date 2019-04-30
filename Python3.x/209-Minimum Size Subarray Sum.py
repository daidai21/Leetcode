# 虫取法
# Runtime: 48 ms, faster than 77.69% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 14.8 MB, less than 12.78% of Python3 online submissions for Minimum Size Subarray Sum.
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        add, start, end, length, minimal = 0, 0, 0, len(nums), float("inf")
        while end < length:
            add += nums[end]
            while add >= s:
                minimal = min(minimal, end - start + 1)
                add -= nums[start]
                start += 1
            end += 1
        return minimal if minimal != float("inf") else 0


'''
two points:


while end < length:
    if add < s:
        end point move
    else:
        update minimal
        start point move
'''


# violence
# using some space exchange some time
# Time Limit Exceeded
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        minimal = length = len(nums)
        sums = [value for value in nums]
        for i in range(1, length):
            sums[i] = sums[i] + sums[i - 1]
        for start in range(length):
            for end in range(start, length):
                if sums[end] - sums[start] + nums[start] >= s:
                    minimal = min(minimal, end - start + 1)
        return minimal


# violence
# Time Limit Exceeded
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        minimal = len(nums)
        for start in range(len(nums)):
            for end in range(start, len(nums) + 1):
                if sum(nums[start:end]) >= s: minimal = min(minimal, end - start)
        return minimal
