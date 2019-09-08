# Runtime: 168 ms, faster than 64.75% of Python3 online submissions for H-Index II.
# Memory Usage: 20.6 MB, less than 50.00% of Python3 online submissions for H-Index II.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length, res = len(citations), 0
        l, r = 0, length - 1
        while l <= r:
            mid = int((l + r) / 2)
            res = max(res, min(citations[mid], length - mid))
            if citations[mid] < length - mid:
                l = mid + 1
            else:
                r = mid - 1
        return res
