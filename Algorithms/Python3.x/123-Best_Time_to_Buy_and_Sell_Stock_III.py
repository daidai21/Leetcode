# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.profit = 0
        self.dfs(prices, -1, 2, 0)
        return self.profit

    def dfs(self, prices, curr, times, profit):
        if times >= 0:
            self.profit = max(self.profit, profit)
        if prices:
            if curr >= 0:  # sell
                for i, price in enumerate(prices):
                    self.dfs(prices[i + 1:], -1, times - 1, profit + prices[i] - curr)
            elif curr == -1:  # buy
                for i, price in enumerate(prices):
                    self.dfs(prices[i + 1:], prices[i], times, profit)


# dp
# Runtime: 96 ms, faster than 40.03% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 15 MB, less than 54.55% of Python3 online submissions for Best Time to Buy and Sell Stock III.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)
        # backward traversal, max_profits record the max profit
        # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])
        return total_max


# dp
# Runtime: 88 ms, faster than 69.69% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 14.8 MB, less than 63.64% of Python3 online submissions for Best Time to Buy and Sell Stock III.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy = float("inf")
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)  # we can buy the second only after first is sold
            two_profit = max(two_profit, p - two_buy)
        return two_profit
