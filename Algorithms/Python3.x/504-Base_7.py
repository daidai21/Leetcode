# Runtime: 36 ms, faster than 73.08% of Python3 online submissions for Base 7.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Base 7.
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return '-' + self.convertToBase7(-num)
        elif num < 7:
            return str(num)
        else:
            return self.convertToBase7(num // 7) + str(num % 7)
