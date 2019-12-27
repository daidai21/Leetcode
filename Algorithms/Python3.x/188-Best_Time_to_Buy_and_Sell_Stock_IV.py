# Runtime: 116 ms, faster than 52.62% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# Memory Usage: 14 MB, less than 66.67% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        len_prices = len(prices)
        # quick solve
        if k >= len_prices / 2:
            profit = 0
            for idx in range(1, len_prices):
                if prices[idx] > prices[idx - 1]:
                    profit += prices[idx] - prices[idx - 1]
            return profit
        # DP
        dp = [[0] * (len_prices) for _ in range(k + 1)]
        for i in range(1, k + 1):
            tmp_max = -prices[0]
            for j in range(1, len_prices):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j - 1] - prices[j])
        return dp[k][-1]
