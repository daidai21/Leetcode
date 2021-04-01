// 1678. Goal Parser Interpretation

// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Goal Parser Interpretation.
// Memory Usage: 6 MB, less than 70.55% of C++ online submissions for Goal Parser Interpretation.
class Solution {
public:
    string interpret(string command) {
        string res;
        for (int i = 0; i < command.size() - 1; ++i) {
            if (command[i] == 'G') {
                res += 'G';
            } else if (command[i] == '(' && command[i + 1] == ')') {
                res += 'o';
                i++;
            } else if (command[i] == 'a' && command[i + 1] == 'l') {
                res += 'a';
                res += 'l';
                i++;
            }
        }
        return command[command.size() - 1] == 'G' ? res + 'G' : res;
    }
};
