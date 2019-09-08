# Runtime: 52 ms, faster than 68.57% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.8 MB, less than 5.34% of Python3 online submissions for Multiply Strings.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


# Runtime: 192 ms, faster than 13.72% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions for Multiply Strings.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i + j] += int(n1) * int(n2)
                res[i + j + 1] += int(res[i + j] / 10)
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return "".join(map(str, res[::-1]))
