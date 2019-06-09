# Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Occurrences After Bigram.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Occurrences After Bigram.
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text = text.split(' ')
        len_text = len(text)
        for i in range(1, len_text - 1):
            if text[i - 1] == first and text[i] == second:
                res.append(text[i + 1])
        return res
