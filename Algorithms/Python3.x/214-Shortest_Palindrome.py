# Runtime: 764 ms, faster than 5.17% of Python3 online submissions for Shortest Palindrome.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Shortest Palindrome.
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for idx in range(len(s), -1, -1):
            tmp = s[idx:][::-1] + s
            if tmp == tmp[::-1]:
                return tmp
        return s
