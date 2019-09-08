class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return s[left + 1:right]

        tmp = ''
        for i in range(len(s)):
            len_1 = palindrome(s, i, i)
            if len(tmp) < len(len_1): tmp = len_1
            len_2 = palindrome(s, i, i + 1)
            if len(tmp) < len(len_2): tmp = len_2
        return tmp


'''
len_1和len_2两种情况：
    len_1:aabaa
    len_2:aabb
'''