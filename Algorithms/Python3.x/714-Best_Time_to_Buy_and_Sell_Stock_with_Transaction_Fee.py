# Runtime: 816 ms, faster than 65.77% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 20.8 MB, less than 12.50% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            # sell or hold last day status, hold money
            cash = max(cash, hold + prices[i] - fee)
            # bug or hold last day status, hold stock
            hold = max(hold, cash - prices[i])
        return cash
