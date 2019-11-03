// Runtime: 136 ms, faster than 88.92% of C++ online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
// Memory Usage: 14.9 MB, less than 100.00% of C++ online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.size(); ++i) {
            cash = max(cash, hold + prices[i] - fee);
            hold = max(hold, cash - prices[i]);
        }
        return cash;
    }
};
