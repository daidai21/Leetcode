# dp & 内存优化
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        min_price, max_profit = prices[0], 0  # 当前最低价 和 当前最大收益
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])  # 买入最低价
            max_profit = max(max_profit, prices[i] - min_price)  # 最大收益比较
        return max_profit
