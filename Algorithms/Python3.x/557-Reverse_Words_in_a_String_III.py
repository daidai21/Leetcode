# Runtime: 40 ms, faster than 72.32% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.1 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])
