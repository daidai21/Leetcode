# Runtime: 44 ms, faster than 31.29% of Python3 online submissions for Buddy Strings.
# Memory Usage: 14.1 MB, less than 8.00% of Python3 online submissions for Buddy Strings.
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(B):
            return True
        diff = [(a, b) for a, b in zip(A, B) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
