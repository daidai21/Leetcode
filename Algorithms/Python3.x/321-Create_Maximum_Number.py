# Runtime: 332 ms, faster than 60.13% of Python3 online submissions for Create Maximum Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Create Maximum Number.
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def prep(nums, k):
            drop = len(nums) - k
            ret = []
            for num in nums:
                while drop and ret and ret[-1] < num:
                    ret.pop()
                    drop -= 1
                ret.append(num)
            return ret[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))
