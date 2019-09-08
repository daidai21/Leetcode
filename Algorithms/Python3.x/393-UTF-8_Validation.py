# Runtime: 120 ms, faster than 92.09% of Python3 online submissions for UTF-8 Validation.
# Memory Usage: 14.2 MB, less than 50.00% of Python3 online submissions for UTF-8 Validation.
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for n in data:
            if count == 0:
                if n >> 5 == 0b110:     count = 1
                elif n >> 4 == 0b1110:  count = 2
                elif n >> 3 == 0b11110: count = 3
                elif n >> 7 == 1:       return False
            else:
                if n >> 6 != 0b10:
                    return False
                count -= 1
        return count == 0
