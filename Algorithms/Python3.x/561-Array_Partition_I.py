# Runtime: 328 ms, faster than 79.52% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.4 MB, less than 6.06% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
