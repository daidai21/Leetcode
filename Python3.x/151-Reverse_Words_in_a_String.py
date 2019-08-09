# Runtime: 36 ms, faster than 75.80% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.4 MB, less than 8.70% of Python3 online submissions for Reverse Words in a String.
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word for word in s.split(' ') if word != ''][::-1])
