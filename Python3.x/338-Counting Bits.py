# Runtime: 132 ms, faster than 52.84% of Python3 online submissions for Counting Bits.
# Memory Usage: 15.9 MB, less than 5.22% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            result.append(result[i >> 1] + (i & 1))
        return result


'''
0 (0, '0b0')
1 (1, '0b1')
1 (2, '0b10')
2 (3, '0b11')
1 (4, '0b100')
2 (5, '0b101')
2 (6, '0b110')
3 (7, '0b111')
1 (8, '0b1000')
2 (9, '0b1001')

find regular
'''


# Runtime: 104 ms, faster than 97.24% of Python3 online submissions for Counting Bits.
# Memory Usage: 15.8 MB, less than 68.15% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        while len(res) <= num:
            res += [x + 1 for x in res]
        return res[:num + 1]
