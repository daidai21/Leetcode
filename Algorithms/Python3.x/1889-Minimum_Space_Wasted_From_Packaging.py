# 二分搜索
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        res = float("inf")
        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]:
                continue
            cur = i = 0
            for b in box:
                j = bisect.bisect(packages, b, i)
                cur += b * (j - i)
                i = j
            res = min(res, cur)
        return (res - sum(packages)) % (10 ** 9 + 7) if res < float("inf") else -1
