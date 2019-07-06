class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        for s in str:
            if 65 <= ord(s) <= 90:
                res += chr(ord(s) + 32)
            else:
                res += s
        return res


class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
