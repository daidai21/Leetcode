# Runtime: 64 ms, faster than 6.55% of Python3 online submissions for Uncommon Words from Two Sentences.
# Memory Usage: 12.4 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dic = {}
        for word in A.split(" ") + B.split(" "):
            dic[word] = dic[word] + 1 if word in dic else 1
        return [word for word in dic if dic[word] == 1]
