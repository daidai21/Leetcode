# Time Limit Exceeded
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 0:
            return 0
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if lower <= pre_sum[j] - pre_sum[i] and upper >= pre_sum[j] - pre_sum[i]:
                    res += 1
        return res


# Runtime: 248 ms, faster than 55.70% of Python3 online submissions for Count of Range Sum.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Count of Range Sum.
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 0:
            return 0
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        def merge_sort(lo, hi):
            mid = lo + (hi - lo) // 2
            if mid == lo:
                return 0
            cnt = merge_sort(lo, mid) + merge_sort(mid, hi)
            i = j = mid
            for left in pre_sum[lo:mid]:
                while i < hi and pre_sum[i] - left < lower:
                    i += 1
                while j < hi and pre_sum[j] - left <= upper:
                    j += 1
                cnt += j - i
            pre_sum[lo:hi] = sorted(pre_sum[lo:hi])
            return cnt

        return merge_sort(0, len(pre_sum))
