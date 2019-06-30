# dp
# Runtime: 40 ms, faster than 69.14% of Python3 online submissions for Decode Ways.
# Memory Usage: 13.3 MB, less than 40.73% of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        dp = [1] + [0 for _ in s]
        for i in range(1, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i != 1 and "09" < s[i - 2:i] < "27":
                dp[i] += dp[i - 2]
        return dp[-1]


# optimize dp in space to O(1)
# Runtime: 48 ms, faster than 19.14% of Python3 online submissions for Decode Ways.
# Memory Usage: 13.1 MB, less than 80.63% of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:
        pre_num, cur_num, pre_c = 0, int(s > ''), ''
        for c in s:
            pre_num, cur_num, pre_c = cur_num, (c > '0') * cur_num + (9 < int(pre_c + c) < 27) * pre_num, c
        return cur_num
