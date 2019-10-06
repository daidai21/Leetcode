# Time Limit Exceeded
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        self.res = 0
        self.recursion("", n)
        return self.res % (10 ** 9 + 7)

    def recursion(self, cur, n):
        if n == 0:
            self.res += 1
        else:
            if cur == "":
                for ch in "aeiou":
                    self.recursion(ch, n - 1)
            else:
                if cur[-1] == 'a':
                    self.recursion(cur + 'e', n - 1)
                elif cur[-1] == 'e':
                    self.recursion(cur + 'a', n - 1)
                    self.recursion(cur + 'i', n - 1)
                elif cur[-1] == 'i':
                    for ch in "aeou":
                        self.recursion(cur + ch, n - 1)
                elif cur[-1] == 'o':
                    self.recursion(cur + 'i', n - 1)
                    self.recursion(cur + 'u', n - 1)
                elif cur[-1] == 'u':
                    self.recursion(cur + 'a', n - 1)


# graph problem, then dp
# Runtime: 224 ms, faster than 50.00% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 19 MB, less than 100.00% of Python3 online submissions for Count Vowels Permutation.
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]
        modulo = 10 ** 9 + 7
        for i in range(5):
            dp[1][i] = 1
        for i in range(1, n):
            dp[i + 1][0] = (dp[i][1] + dp[i][2] + dp[i][4]) % modulo  # a
            dp[i + 1][1] = (dp[i][0] + dp[i][2]) % modulo  # e
            dp[i + 1][2] = (dp[i][1] + dp[i][3]) % modulo  # i
            dp[i + 1][3] = (dp[i][2]) % modulo  # o
            dp[i + 1][4] = (dp[i][2] + dp[i][3]) % modulo  # u
        return sum(dp[n]) % modulo
