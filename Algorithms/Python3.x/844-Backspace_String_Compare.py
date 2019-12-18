# Runtime: 28 ms, faster than 88.25% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ""
        for i in S:
            if i == '#':
                s = s[:-1]
            else:
                s = s + i
        t = ""
        for i in T:
            if i == '#':
                t = t[:-1]
            else:
                t = t + i
        return s == t


# Runtime: 32 ms, faster than 70.81% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ""
        for i in S:
            s = s[:-1] if i == '#' else s + i
        t = ""
        for i in T:
            t = t[:-1] if i == '#' else t + i
        return s == t


# two pointer
# Runtime: 28 ms, faster than 88.25% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        back_S, back_T = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == '#' or back_S > 0):
                back_S = back_S + 1 if S[i] == '#' else back_S - 1
                i -= 1
            while j >= 0 and (T[j] == '#' or back_T > 0):
                back_T = back_T + 1 if T[j] == '#' else back_T - 1
                j -= 1
            if S[i] != T[j]:
                return False
            i, j = i - 1, j - 1
        return i == j
