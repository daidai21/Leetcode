# Runtime: 72 ms, faster than 56.96% of Python3 online submissions for Single Number III.
# Memory Usage: 15.7 MB, less than 50.00% of Python3 online submissions for Single Number III.
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mem = set()
        for num in nums:
            if num in mem:
                mem.remove(num)
            else:
                mem.add(num)
        return list(mem)
