# Runtime: 64 ms, faster than 91.46% of Python3 online submissions for Single Number II.
# Memory Usage: 16 MB, less than 5.88% of Python3 online submissions for Single Number II.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s1, s2 = set(), set()  # s1 is the first appear, s2 is already repeat appear
        for num in nums:
            if num in s2:
                pass
            elif num in s1:
                s1.remove(num)
                s2.add(num)
            else:
                s1.add(num)
        return s1.pop()


# Runtime: 68 ms, faster than 76.42% of Python3 online submissions for Single Number II.
# Memory Usage: 15.9 MB, less than 5.88% of Python3 online submissions for Single Number II.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = set(nums)
        tmp = sum(tmp) * 3 - sum(nums)
        return int(tmp / 2)
