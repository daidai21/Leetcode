# greedy
# Runtime: 116 ms, faster than 43.75% of Python3 online submissions for Jump Game II.
# Memory Usage: 16.1 MB, less than 8.33% of Python3 online submissions for Jump Game II.
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = 0  # current arrive the farthest index
        i = 0
        while cur < len(nums) - 1:
            res += 1
            pre = cur  # previous arrive the farthest index
            while i <= pre:
                cur = max(cur, i + nums[i])
                i += 1
            # if pre == cur:  # not update, unbale to reach the farthest position
            #     return -1
        return res
