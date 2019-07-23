# Runtime: 272 ms, faster than 25.00% of Python3 online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 23.5 MB, less than 100.00% of Python3 online submissions for Number of Equivalent Domino Pairs.
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic, res = {}, 0
        for a, b in dominoes:
            key = min(a, b) * 10 + max(a, b)
            if dic.__contains__(key):
                res += dic[key]
                dic[key] += 1
            else:
                dic[key] = 1
        return res
