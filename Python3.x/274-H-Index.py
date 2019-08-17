# Runtime: 40 ms, faster than 93.37% of Python3 online submissions for H-Index.
# Memory Usage: 14 MB, less than 14.29% of Python3 online submissions for H-Index.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
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


# Runtime: 40 ms, faster than 93.37% of Python3 online submissions for H-Index.
# Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for H-Index.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        length, res = len(citations), 0
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            res = max(res, min(citations[mid], mid + 1))
            if citations[mid] > mid + 1:
                l = mid + 1
            else:
                r = mid - 1
        return res
