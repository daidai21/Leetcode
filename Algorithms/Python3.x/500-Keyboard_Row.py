# Runtime: 32 ms, faster than 90.11% of Python3 online submissions for Keyboard Row.
# Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Keyboard Row.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        res = []
        for word in words:
            can = True
            line = None
            for ch in word:
                if line is None:
                    for i, kb in enumerate(keyboard):
                        if ch.lower() in kb:
                            line = i
                else:
                    if ch.lower() not in keyboard[line]:
                        can = False
                        break
            if can:
                res.append(word)
        return res
