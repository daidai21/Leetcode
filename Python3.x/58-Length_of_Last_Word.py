class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for w in s.split(' '):
            if w != '':
                res = len(w)
        return res


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])


# two pointer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        slow = len_s - 1
        while slow >= 0 and s[slow] == ' ':
            slow -= 1
        fast = slow
        while fast >= 0 and s[fast] != ' ':
            fast -= 1
        return slow - fast