# Runtime: 52 ms, faster than 29.55% of Python3 online submissions for Subsets II.
# Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Subsets II.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def recursion(idx, curr):
            if idx == len(nums):
                if curr not in res:
                    res.append(curr)
            else:
                recursion(idx + 1, curr)
                recursion(idx + 1, curr + [nums[idx]])

        recursion(0, [])
        return res
