# Runtime: 328 ms, faster than 97.66% of Python3 online submissions for Longest Harmonious Subsequence.
# Memory Usage: 14.4 MB, less than 69.23% of Python3 online submissions for Longest Harmonious Subsequence.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic[num] + 1 if num in dic else 1
        res = 0
        for key, val in dic.items():
            if key + 1 in dic:
                res = max(res, dic[key] + dic[key + 1])
        return res

