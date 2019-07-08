class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            tmp, number, previous = "", 1, res[0]
            for c in res[1:]:
                if c == previous:
                    number += 1
                else:
                    tmp += str(number) + previous
                    number, previous = 1, c
            tmp += str(number) + previous
            res = tmp
        return res
