# Runtime: 40 ms, faster than 67.83% of Python3 online submissions for Gray Code.
# Memory Usage: 13.8 MB, less than 6.03% of Python3 online submissions for Gray Code.
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x + 2 ** i for x in reversed(res)]
        return res


'''
from up to down, then left to right

0   1   11  110
        10  111
            101
            100
            
start:      [0]
i = 0:      [0, 1]
i = 1:      [0, 1, 3, 2]
i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
'''