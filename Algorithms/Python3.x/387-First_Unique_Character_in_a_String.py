# Runtime: 116 ms, faster than 71.77% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 13.1 MB, less than 96.46% of Python3 online submissions for First Unique Character in a String.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        index = 0
        for c in s:
            if count[c] == 1:
                return index
            else:
                index += 1
        return -1


# Runtime: 128 ms, faster than 55.99% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 13.4 MB, less than 30.45% of Python3 online submissions for First Unique Character in a String.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            if c not in dic: dic[c] = 1
            else: dic[c] += 1
        for i, v in enumerate(s):
            if dic[v] == 1: return i
        return -1
