# Runtime: 56 ms, faster than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(num)) % 2 == 0 for num in nums])
