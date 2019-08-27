# Runtime: 44 ms, faster than 43.33% of Python3 online submissions for Most Common Word.
# Memory Usage: 13.5 MB, less than 5.88% of Python3 online submissions for Most Common Word.
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        dic = {}
        res = ""
        count = 0
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
            if dic[word] > count:
                count = dic[word]
                res = word
        return res
