# Runtime: 32 ms, faster than 51.88% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 13.8 MB, less than 14.29% of Python3 online submissions for Long Pressed Name.
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            cur_i = name[i]
            cur_j = typed[j]
            if cur_i != cur_j:
                return False
            tmp_i, tmp_j = 0, 0  # char repeat num
            while i < len(name) and name[i] == cur_i:
                i += 1
                tmp_i += 1
            while j < len(typed) and typed[j] == cur_j:
                j += 1
                tmp_j += 1
            if tmp_i > tmp_j:
                return False
        return False if i < len(name) or j < len(typed) else True
