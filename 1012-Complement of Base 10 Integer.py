# 
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        X = 1
        while N > X: X = X * 2 + 1
        return X - N


'''
首先找到一个数 X = 111111111... >= N
而且，必须注意的是，N = 0，是一个预期结果为 1 的情况

N + bitwiseComplement(N) = 11....11 = X
所以 bitwiseComplement(N) = X - N
'''


# 常规操作
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary_N = bin(N)[2:]  # exchange to binary
        result = ''
        for i in binary_N:  # 0 and 1 转换
            if i == '1':
                result += '0'
                continue
            result += '1'
        return int(result, 2)


# one lines
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(bin(N)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)
