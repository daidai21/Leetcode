// Runtime: 4 ms, faster than 63.12% of C++ online submissions for Path In Zigzag Labelled Binary Tree.
// Memory Usage: 8.5 MB, less than 100.00% of C++ online submissions for Path In Zigzag Labelled Binary Tree.
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        int level = 0;
        while (1 << level <= label)
            ++level;
        vector<int> res(level);
        for (; label >= 1; label /= 2, --level) {
            res[level - 1] = label;
            label = (1 << level) - 1 + (1 << (level - 1)) - label;
        }
        return res;
    }
};
