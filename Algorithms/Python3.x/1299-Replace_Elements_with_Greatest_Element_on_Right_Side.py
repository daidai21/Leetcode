# Runtime: 96 ms, faster than 14.38% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        pre = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            res[i] = max(arr[i + 1], pre)
            pre = max(pre, arr[i + 1])
        return res
