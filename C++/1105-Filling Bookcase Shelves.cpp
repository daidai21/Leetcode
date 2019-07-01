// Runtime: 4 ms, faster than 98.71% of C++ online submissions for Filling Bookcase Shelves.
// Memory Usage: 9.5 MB, less than 100.00% of C++ online submissions for Filling Bookcase Shelves.
class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelf_width) {
        vector<int> dp(books.size() + 1, INT16_MAX);
        dp[0] = 0;
        for (int i = 1; i <= books.size(); ++i) {
            int max_width = books[i - 1][0];
            int max_height = books[i - 1][1];
            dp[i] = dp[i - 1] + max_height;
            for (int j = i - 1; j > 0; --j) {
                max_width += books[j - 1][0];
                max_height = max(max_height, books[j - 1][1]);
                if (max_width > shelf_width)
                    break;
                dp[i] = min(dp[i], dp[j - 1] + max_height);
            }
        }
        return dp[books.size()];
    }
};
