# Runtime: 92 ms, faster than 78.92% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # choose element
        vals = []
        len_arr = len(arr)
        for i in range(10):
            vals.append(arr[int(len_arr / 10.0 * i)])
        # calcuate the maximum number of appear
        res = vals[0]
        cnt = vals.count(vals[0])  # number of arr[0] appear
        for val in vals:
            if vals.count(val) > cnt:
                res = val
                cnt = vals.count(val)
        return res


# Runtime: 104 ms, faster than 18.76% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        len_arr = len(arr)
        tmp = int(len_arr / 4.0)
        for idx in range(int(len_arr * 3.0 / 4.0)):
            if arr[idx] == arr[idx + tmp]:
                return arr[idx]
        return arr[-1]
