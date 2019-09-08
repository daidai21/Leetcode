# Runtime: 112 ms, faster than 45.21% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 21.7 MB, less than 25.00% of Python3 online submissions for Contains Duplicate II.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                return True
            dic[num] = i
        return False
