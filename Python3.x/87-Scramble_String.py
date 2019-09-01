# recursion
# Runtime: 44 ms, faster than 89.88% of Python3 online submissions for Scramble String.
# Memory Usage: 13.8 MB, less than 33.33% of Python3 online submissions for Scramble String.
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 != len_s2 or sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        for i in range(1, len_s1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
               self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
