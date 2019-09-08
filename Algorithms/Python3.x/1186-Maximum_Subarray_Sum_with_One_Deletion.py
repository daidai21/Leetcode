# dp
# Runtime: 304 ms, faster than 100.00% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
# Memory Usage: 24.6 MB, less than 100.00% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ignored = 0
        notignored = 0
        result = arr[0]
        for i in arr:
            if i >= 0:
                ignored += i
                notignored += i
            else:
                notignored = max(notignored + i, ignored)
                ignored += i
            result = max(result, notignored if notignored != 0 else float("-inf"), ignored if ignored != 0 else float("-inf"))
            ignored, notignored = max(ignored, 0), max(notignored, 0)
        return max(result, max(arr))


# dp
# Runtime: 304 ms, faster than 100.00% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
# Memory Usage: 24.6 MB, less than 100.00% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        len_arr = len(arr)
        if len_arr == 1:
            return arr[0]
        curr_sum_del = 0
        curr_sum = arr[0]
        result = curr_sum
        for i in range(1, len_arr):
            curr_sum_del = max(curr_sum_del + arr[i - 1], arr[i - 1])
            curr_sum = max(curr_sum + arr[i], curr_sum_del, arr[i])
            result = max(result, curr_sum)
        return result
