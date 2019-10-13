class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_split = 0
        l = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            else:
                l -= 1
            if l == 0:
                max_split += 1
                l = 0
        return max_split
