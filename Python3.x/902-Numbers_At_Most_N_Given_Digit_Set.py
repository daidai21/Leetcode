# Dynamic Programming + Counting
# Runtime: 40 ms, faster than 50.44% of Python3 online submissions for Numbers At Most N Given Digit Set.
# Memory Usage: 13.2 MB, less than 25.00% of Python3 online submissions for Numbers At Most N Given Digit Set.
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        for i in range(K - 1, -1, -1):
            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i+1]
        return dp[0] + sum(len(D) ** i for i in range(1, K))


'''
（1）首先明确一个问题，就是给的数字集合 D 是不重复的，感觉这一点还是很重要的。 
（2）假设数字 N 为 K 位， 很显然，K-1 的数字一定比它小，那么能组成 K-1 位的数有多少那？答案为(K-1)^(len(D))，理解就是每一位有 len(D) 种选择，所以是它的次方个。 
（3）由（2）可以求出位数为1 - (K-1) 位 的数的个数了，现在位数为 K，其比 N 小的数字怎么求？动态规划方法。 
（4）–求位数为K且小于 N 的数字个数–， 思路： 
（5）从数据集D中依次拿出 一个数去和N的最高位比较，如果比它小，后面各个位上的数字可以任意组合，通过求次方就可以得到。 
（6）如果比它小，很显然，后面再怎么组合也是不符合要求的，所以直接舍弃。 
（7）如果相等，现在也很显然，竟然最高位相等，那么就可以直接等于次高位符合要求的个数（形成子问题 – 动态规划的一个必要条件）。然后把所有的累加，就是位数为 K 且小于N的数字个数。
'''


# optimize
# Runtime: 36 ms, faster than 74.34% of Python3 online submissions for Numbers At Most N Given Digit Set.
# Memory Usage: 13.1 MB, less than 25.00% of Python3 online submissions for Numbers At Most N Given Digit Set.
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        S, K, dp = str(N), len(str(N)), [0] * len(str(N)) + [1]
        for i in range(K - 1, -1, -1):
            for d in D:
                if d < S[i]: dp[i] += len(D) ** (K - i - 1)
                elif d == S[i]: dp[i] += dp[i+1]
        return dp[0] + sum(len(D) ** i for i in range(1, K))
