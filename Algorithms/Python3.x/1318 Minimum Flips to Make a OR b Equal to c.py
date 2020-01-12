class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        len_a = len(bin(a)[2:])
        len_b = len(bin(b)[2:])
        len_c = len(bin(c)[2:])
        a = list([int(i) for i in bin(a)[2:][::-1]]) + [0] * 9
        b = list([int(i) for i in bin(b)[2:][::-1]]) + [0] * 9
        c = list([int(i) for i in bin(c)[2:][::-1]]) + [0] * 9
        res = 0
        for i in range(max(len_a, len_b, len_c)):
            if c[i] == 1:
                if a[i] == 0 and b[i] == 0:
                    res += 1
            else:  # c[i] == 0
                res += a[i] == 1
                res += b[i] == 1
        return res


print(Solution().minFlips(2, 6, 5))  # 3
print(Solution().minFlips(4, 2, 7))  # 1
print(Solution().minFlips(1, 2, 3))  # 0
print(Solution().minFlips(8, 3, 5))  # 3
print(bin(8)[2:], bin(3)[2:], bin(5)[2:])
