// Runtime: 12 ms, faster than 69.34% of C++ online submissions for Diameter of Binary Tree.
// Memory Usage: 19.7 MB, less than 92.59% of C++ online submissions for Diameter of Binary Tree.
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
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0;
        dfs(root, res);
        return res;
    }
private:
    int dfs(TreeNode* node, int& res) {
        if (!node)
            return 0;
        int left = dfs(node->left, res);
        int right = dfs(node->right, res);
        res = max(res, left + right);
        return max(left, right) + 1;
    }
};
