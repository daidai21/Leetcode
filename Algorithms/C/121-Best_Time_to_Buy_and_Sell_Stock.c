// Runtime: 804 ms, faster than 16.65% of C online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 8 MB, less than 50.00% of C online submissions for Best Time to Buy and Sell Stock.
int maxProfit(int* prices, int pricesSize){
    int profit = 0;
    for (int i = 0; i < pricesSize - 1; ++i)
        for (int j = i + 1; j < pricesSize; ++j)
            if (*(prices + j) - *(prices + i) > profit)
                profit = *(prices + j) - *(prices + i);
    return profit;
}


// Runtime: 8 ms, faster than 66.70% of C online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 7.8 MB, less than 100.00% of C online submissions for Best Time to Buy and Sell Stock.
int maxProfit(int* prices, int pricesSize){
    int min_price = INT_MAX;
    int max_profit = 0;
    for (int i = 0; i < pricesSize; ++i)
        if (*(prices + i) < min_price)
            min_price = *(prices + i);
        else if (*(prices + i) - min_price > max_profit)
            max_profit = *(prices + i) - min_price;
    return max_profit;
}

