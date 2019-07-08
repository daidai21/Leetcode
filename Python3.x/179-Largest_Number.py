# Runtime: 52 ms, faster than 35.65% of Python3 online submissions for Largest Number.
# Memory Usage: 13.1 MB, less than 76.78% of Python3 online submissions for Largest Number.
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums = [str(num) for num in nums]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)


# Runtime: 16 ms, faster than 98.97% of Python online submissions for Largest Number.
# Memory Usage: 11.9 MB, less than 20.83% of Python online submissions for Largest Number.
# Python2.x
class Solution(object):
    def largestNumber(self, nums):
        res = ''.join(sorted(map(str, nums),
                    lambda x, y: -1 if x + y > y + x else 1)
                    )
        return res.lstrip('0') or '0'
