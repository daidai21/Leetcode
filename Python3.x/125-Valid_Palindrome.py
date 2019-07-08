class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        return s == s[::-1]


# Runtime: 60 ms, faster than 62.00% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.4 MB, less than 71.81% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() !=  s[end].lower():
                return False
            start, end = start + 1, end - 1
        return True