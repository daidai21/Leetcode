# Runtime: 36 ms, faster than 84.94% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Longest Palindrome.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        se = set()
        for c in s:
            if c not in se:
                se.add(c)
            else:
                se.remove(c)
        return len(s) - len(se) + 1 if len(se) > 0 else len(s)  # len(hash) is the number of the odd letters
