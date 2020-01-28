# Bit manipulation
# Runtime: 184 ms, faster than 96.21% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Maximum Product of Word Lengths.
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            mask = 0
            for ch in set(word):
                mask |= (1 << (ord(ch) - 97))
            dic[mask] = max(dic.get(mask, 0), len(word))
        return max([dic[x] * dic[y] for x in dic for y in dic if not x & y] or [0])
