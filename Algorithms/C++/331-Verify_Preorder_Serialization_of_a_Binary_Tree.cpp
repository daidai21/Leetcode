#include <string>
#include <vector>
#include <sstream>
#include <iostream>
using namespace std;


// Runtime: 12 ms, faster than 41.85% of C++ online submissions for Verify Preorder Serialization of a Binary Tree.
// Memory Usage: 10 MB, less than 12.50% of C++ online submissions for Verify Preorder Serialization of a Binary Tree.
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int diff = 1; // diff = outdegree - indegree
        vector<string> nodes = this->split(preorder, ',');
        for (string& node : nodes) {
            if (--diff < 0) {
                return false;
            }
            if (node != "#")
                diff += 2;
        }
        return diff == 0;
    }

private:
    vector<string> split(string str, char sep) {
        stringstream s(str);
        string temp;
        vector<string> res;
        while (getline(s, temp, sep)) {
            res.push_back(temp);
        }
        return res;
    }
};
