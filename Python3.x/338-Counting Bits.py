# Runtime: 132 ms, faster than 52.84% of Python3 online submissions for Counting Bits.
# Memory Usage: 15.9 MB, less than 5.22% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            result.append(result[i >> 1] + (i & 1))
        return result


'''
(0, '0b0')
(1, '0b1')
(2, '0b10')
(3, '0b11')
(4, '0b100')
(5, '0b101')
(6, '0b110')
(7, '0b111')
(8, '0b1000')
(9, '0b1001')

find regular
'''
