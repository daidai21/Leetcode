# Time Limit Exceeded
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest = 0
        for start in range(len(arr)):
            cur = start
            long = 1
            cur_val = arr[cur]
            while cur + 1 < len(arr):
                if arr[cur + 1] - cur_val == difference:
                    long += 1
                    cur_val = arr[cur + 1]
                cur += 1
            longest = max(longest, long)
        return longest


# dp (using dict change time)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = float("-inf")
        dic = {}  # k is num, v is count
        for n in arr:
            count = 1
            if n - difference in dic:
                count += dic[n - difference]
            dic[n] = max(dic[n], count) if n in dic else count
            res = max(res, count)
        return res
