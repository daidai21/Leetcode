# Runtime: 40 ms, faster than 95.69% of Python3 online submissions for Missing Number.
# Memory Usage: 14.3 MB, less than 14.16% of Python3 online submissions for Missing Number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)
        for num in nums: 
            arr[num] = 1
        for i, val in enumerate(arr[1:]):
            if val == 0: return i + 1
        return 0
