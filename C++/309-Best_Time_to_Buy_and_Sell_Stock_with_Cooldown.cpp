// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Best Time to Buy and Sell Stock with Cooldown.
// Memory Usage: 8.6 MB, less than 92.59% of C++ online submissions for Best Time to Buy and Sell Stock with Cooldown.
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int free = 0, have = INT_MIN, cool = INT_MIN;
        for (int p : prices) {
            int temp0 = free, temp1 = have, temp2 = cool;
            free = max(free, temp2);
            have = max(have, temp0 - p);
            cool = temp1 + p;
        }
        return max(free, cool);
    }
};


/*
free is the maximum profit I can have while being free to buy.
是我在免费购买的同时可以获得的最大利润。  表示第i天前，任何以buy状态结尾的交易序列所获得的最大利润
have is the maximum profit I can have while having stock.
是我拥有股票时能获得的最大利润。  表示第i天前，任何以sell状态结尾的交易序列所获得的最大利润
cool is the maximum profit I can have while cooling down.
是我在冷却的同时所能获得的最大利润。  表示第i天前，任何以rest状态结尾的交易序列所获得的最大利润
*/


// TODO: 样例可能补全，本身有bug，但可以pass
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int free = 0, have = INT_MIN, cool = INT_MIN;
        for (int p : prices) {
            int temp0 = free, temp2 = cool;
            free = max(free, temp2);
            have = max(have, temp0 - p);
            cool = have + p;
        }
        return max(free, cool);
    }
};
// Runtime: 4 ms, faster than 74.89% of C++ online submissions for Best Time to Buy and Sell Stock with Cooldown.
// Memory Usage: 8.8 MB, less than 33.33% of C++ online submissions for Best Time to Buy and Sell Stock with Cooldown.