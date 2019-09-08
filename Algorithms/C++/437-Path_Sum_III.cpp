// Runtime: 24 ms, faster than 55.72% of C++ online submissions for Path Sum III.
// Memory Usage: 14.4 MB, less than 100.00% of C++ online submissions for Path Sum III.
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
    int pathSum(TreeNode* root, int sum) {
        dfs(root, sum);
        return result;
    }
private:
    int result = 0;
    void dfs(TreeNode* node, int sum) {
        if (!node)
            return;
        judge(node, sum);
        dfs(node->left, sum);
        dfs(node->right, sum);
    }

    void judge(TreeNode* node, int sum) {
        if (!node)
            return;
        if (node->val == sum)
            ++result;
        judge(node->left, sum - node->val);
        judge(node->right, sum - node->val);
    }
};
