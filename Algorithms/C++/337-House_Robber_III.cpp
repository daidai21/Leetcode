// Runtime: 8 ms, faster than 99.21% of C++ online submissions for House Robber III.
// Memory Usage: 20.5 MB, less than 100.00% of C++ online submissions for House Robber III.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {
        return dfs(root).second;
    }
private:
    pair<int, int> dfs(TreeNode* node) {
        if (!node)
            return make_pair(0, 0);
        pair<int, int> l = dfs(node->left);
        pair<int, int> r = dfs(node->right);
        int f2 = l.second + r.second;                    // subtree max val
        int f1 = max(f2, l.first + r.first + node->val); // current node max val
        return make_pair(f2, f1);
    }
};
