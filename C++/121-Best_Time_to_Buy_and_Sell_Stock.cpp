// Brute Force
// Runtime: 1664 ms, faster than 5.00% of C++ online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 9.5 MB, less than 84.40% of C++ online submissions for Best Time to Buy and Sell Stock.
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        for (int i = 0; i < prices.size(); ++i)
            for (int j = i + 1; j < prices.size(); ++j)
                res = max(res, prices[j] - prices[i]);
        return res;
    }
};


// Runtime: 4 ms, faster than 98.29% of C++ online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 9.6 MB, less than 74.31% of C++ online submissions for Best Time to Buy and Sell Stock.
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0, min_price = INT_MAX;
        for (int i = 0; i < prices.size(); ++i) {
            min_price = min(min_price, prices[i]);
            max_profit = max(max_profit, prices[i] - min_price);
        }
        return max_profit;
    }
};
