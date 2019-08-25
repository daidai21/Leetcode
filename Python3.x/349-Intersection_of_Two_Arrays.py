# Runtime: 244 ms, faster than 5.30% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Intersection of Two Arrays.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for i1 in range(len(nums1)):
            for i2 in range(len(nums2)):
                if nums1[i1] == nums2[i2]:
                    res.add(nums1[i1])
                    nums2[i2] = None
        return list(res)
