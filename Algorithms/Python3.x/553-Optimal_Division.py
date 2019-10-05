# Runtime: 36 ms, faster than 74.39% of Python3 online submissions for Optimal Division.
# Memory Usage: 13.9 MB, less than 33.33% of Python3 online submissions for Optimal Division.
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        len_nums = len(nums)
        if len_nums == 0:
            return ""
        elif len_nums == 1:
            return str(nums[0])
        elif len_nums == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            res = str(nums[0]) + "/(" + str(nums[1])
            for i in range(2, len_nums):
                res += "/" + str(nums[i])
        return res + ")"
