# Runtime: 44 ms, faster than 6.58% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.9 MB, less than 16.67% of Python3 online submissions for Summary Ranges.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return [str(nums[0])]
        l, r = 0, 1
        res = []
        while r <= n:
            while r < n and nums[r] == nums[r - 1] + 1:
                r += 1
            if r == l + 1:
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l]) + "->" + str(nums[r - 1]))
            l = r
            r += 1
        return res
