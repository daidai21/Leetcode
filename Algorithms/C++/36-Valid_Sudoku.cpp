// Runtime: 12 ms, faster than 89.79% of C++ online submissions for Valid Sudoku.
// Memory Usage: 10 MB, less than 56.41% of C++ online submissions for Valid Sudoku.
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // check every column
        for (int i = 0; i < board.size(); ++i) {
            vector<char> visited;
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] != '.')
                    if (find(visited.begin(), visited.end(), board[i][j]) != visited.end())
                        return false;
                    else
                        visited.push_back(board[i][j]);
            }
        }
        // check every row
        for (int j = 0; j < board[0].size(); ++j) {
            vector<char> visited;
            for (int i = 0; i < board[0].size(); ++i) {
                if (board[i][j] != '.')
                    if (find(visited.begin(), visited.end(), board[i][j]) != visited.end())
                        return false;
                    else
                        visited.push_back(board[i][j]);
            }
        }
        // check 3 x 3 sub-boxes
        for (int row = 0; row < 3; ++row) { // sub-box row
            for (int col = 0; col < 3; ++col) { // sub-box col
                vector<char> visited;
                for (int i = row * 3; i < row * 3 + 3; ++i)
                    for (int j = col * 3; j < col * 3 + 3; ++j)
                        if (board[i][j] != '.')
                            if (find(visited.begin(), visited.end(), board[i][j]) != visited.end())
                                return false;
                            else
                                visited.push_back(board[i][j]);
            }
        }
        return true;
    }
};
