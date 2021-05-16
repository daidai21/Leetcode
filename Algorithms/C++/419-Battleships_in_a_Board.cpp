// Runtime: 8 ms, faster than 69.62% of C++ online submissions for Battleships in a Board.
// Memory Usage: 8 MB, less than 78.03% of C++ online submissions for Battleships in a Board.
// 统计左上角

class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int cnt = 0;
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == 'X' && 
                    (i == 0 || board[i - 1][j] != 'X') &&
                    (j == 0 || board[i][j - 1] != 'X'))
                    cnt++;
            }
        }
        return cnt;
    }
};


