# Time Limit Exceeded
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                temp = s[:i] + s[i + 1:]
                if temp == temp[::-1]:
                    return True
        return False


# Runtime: 152 ms, faster than 55.98% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 14.3 MB, less than 6.25% of Python3 online submissions for Valid Palindrome II.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s) / 2 and s[i] == s[-i - 1]:
            i += 1
        s = s[i:len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
