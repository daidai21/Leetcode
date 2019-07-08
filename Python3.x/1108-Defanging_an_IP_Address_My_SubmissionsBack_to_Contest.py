class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', "[.]")


class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for ch in address:
            if ch == '.':
                res += "[.]"
            else:
                res += ch
        return res
