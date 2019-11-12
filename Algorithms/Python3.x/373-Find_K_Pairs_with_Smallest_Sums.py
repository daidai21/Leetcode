# Runtime: 340 ms, faster than 25.80% of Python3 online submissions for Find K Pairs with Smallest Sums.
# Memory Usage: 47.6 MB, less than 11.11% of Python3 online submissions for Find K Pairs with Smallest Sums.
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        for num1 in nums1:
            for num2 in nums2:
                ans.append([num1, num2])
        return sorted(ans, key=lambda x: x[0] + x[1])[:k]


# Runtime: 320 ms, faster than 27.69% of Python3 online submissions for Find K Pairs with Smallest Sums.
# Memory Usage: 47.5 MB, less than 11.11% of Python3 online submissions for Find K Pairs with Smallest Sums.
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return sorted([[n1, n2] for n1 in nums1 for n2 in nums2], key=lambda x: x[0] + x[1])[:k]
