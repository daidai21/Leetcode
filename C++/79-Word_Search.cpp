// Runtime: 16 ms, faster than 98.95% of C++ online submissions for Word Search.
// Memory Usage: 10 MB, less than 100.00% of C++ online submissions for Word Search.
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        len_row = board.size();
        len_col = board[0].size();
        for (int row = 0; row < len_row; ++row)
            for (int col = 0; col < len_col; ++col)
                if (is_found(board, word.c_str(), row, col))
                    return true;
        return false;
    }
private:
    int len_row, len_col;
    bool is_found(vector<vector<char>>& board, const char* w, int row, int col) {
        if (row < 0 || col < 0 || row >= len_row || col >= len_col || board[row][col] == '\0' || board[row][col] != *w)
            return false;
        if (*(w + 1) == '\0')
            return true;
        char temp = board[row][col];
        board[row][col] = '\0';
        if (is_found(board, w + 1, row - 1, col) || is_found(board, w + 1, row + 1, col) ||
            is_found(board, w + 1, row, col - 1) || is_found(board, w + 1, row, col + 1))
            return true;
        board[row][col] = temp;
        return false;
    }
};
