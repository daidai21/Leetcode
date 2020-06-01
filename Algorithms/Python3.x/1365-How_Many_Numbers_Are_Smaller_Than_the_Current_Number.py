# Runtime: 56 ms, faster than 81.56% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnts = [0] * 101
        res = [None] * len(nums)
        for num in nums:
            cnts[num] += 1
        for i in range(1, 101):
            cnts[i] += cnts[i - 1]
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = cnts[nums[i] - 1]
        return res
