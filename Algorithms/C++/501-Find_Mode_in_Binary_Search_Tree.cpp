// Runtime: 24 ms, faster than 71.10% of C++ online submissions for Find Mode in Binary Search Tree.
// Memory Usage: 23.2 MB, less than 85.71% of C++ online submissions for Find Mode in Binary Search Tree.
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
    vector<int> findMode(TreeNode* root) {
        dfs(root);
        return this->result;
    }

private:
    void dfs(TreeNode* node) {
        if (node == nullptr)
            return ;
        dfs(node->left);
        if (node->val == pre_val)
            cur_freq++;
        else
            cur_freq = 1;
        if (cur_freq == max_freq)
            result.push_back(node->val);
        else if (cur_freq > max_freq) {
            result.resize(0);
            result.push_back(node->val);
            max_freq = cur_freq;
        }
        pre_val = node->val;
        dfs(node->right);
    }

    vector<int> result;
    int pre_val;
    int max_freq = 0;
    int cur_freq = 0;
};
