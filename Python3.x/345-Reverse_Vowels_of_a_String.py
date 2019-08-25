# Time Limit Exceeded
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        temp = []
        s = list(s)
        for i, c in enumerate(s):
            if c in vowels:
                temp.append(c)
                s[i] = None
        for t in temp[::-1]:
            for i, c in enumerate(s):
                if c is None:
                    s[i] = t
                    break
        return ''.join(s)


# Runtime: 112 ms, faster than 33.23% of Python online submissions for Reverse Vowels of a String.
# Memory Usage: 13.8 MB, less than 100.00% of Python online submissions for Reverse Vowels of a String.
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) - 1 and l < r and s[l] not in vowels:
                l += 1
            while r > 0 and l < r and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
