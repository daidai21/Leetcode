# 想想成为峰谷
# Runtime: 40 ms, faster than 88.78% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 14 MB, less than 29.13% of Python3 online submissions for Best Time to Buy and Sell Stock II.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        res, pred = 0, prices[0]
        for price in prices[1:]:
            if price > pred: res += price - pred
            pred = price
        return res
