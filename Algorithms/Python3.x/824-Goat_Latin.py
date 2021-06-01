# Runtime: 16 ms, faster than 99.93% of Python3 online submissions for Goat Latin.
# Memory Usage: 14.1 MB, less than 90.41% of Python3 online submissions for Goat Latin.
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        res = ""
        for i, word in enumerate(words):
            res += (word if word[0] in 'aeiouAEIOU' else word[1:] + word[0]) + 'ma'
            res += (i + 1) * 'a' + ' '
        return res[:-1]
