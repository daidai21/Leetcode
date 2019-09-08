# Runtime: 172 ms, faster than 6.23% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 13.2 MB, less than 70.29% of Python3 online submissions for Intersection of Two Arrays II.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i, val1 in enumerate(nums1):
            for j, val2 in enumerate(nums2):
                if val1 == val2:
                    res.append(val1)
                    nums2[j] = None
                    break
        return res
