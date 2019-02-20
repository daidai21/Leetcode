# dp
# Runtime: 40 ms, faster than 93.79% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 12.5 MB, less than 82.89% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        free, have, cool = 0, float("-inf"), float("-inf")
        for price in prices:
            free, have, cool = max(free, cool), max(have, free - price), have + price
        return max(free, cool)


'''
状态机的思路
三种状态：
    free 卖股票 没有
    have 买股票 持有
    cool 不交易 冷却
五种转换：
    持有 ==不做什么==》 持有
    持有 ==卖出==》 冷却
    没有 ==不交易==》 没有
    没有 ==买入==》 持有
    冷却 ==不做什么==》 不持有
'''
