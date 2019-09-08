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
    TreeNode* bstToGst(TreeNode* root) {
        if (root->right)
            bstToGst(root->right);
        val += root->val;
        root->val = val;
        if (root->left)
            bstToGst(root->left);
        return root;
    }
private:
    int val = 0;
};