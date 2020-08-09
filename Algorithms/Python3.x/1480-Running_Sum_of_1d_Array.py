# Runtime: 32 ms, faster than 97.72% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.1 MB, less than 27.42% of Python3 online submissions for Running Sum of 1d Array.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        sum_num = 0
        idx = 0
        for num in nums:
            sum_num += num
            res[idx] = sum_num
            idx += 1
        return res
