// Runtime: 4 ms, faster than 83.66% of C++ online submissions for Symmetric Tree.
// Memory Usage: 14.7 MB, less than 93.22% of C++ online submissions for Symmetric Tree.
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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        return judge(root->left, root->right);
    }
private:
    bool judge(TreeNode* left, TreeNode* right) {
        if (left == NULL || right == NULL)
            return left == right;
        if (left->val != right->val)
            return false;
        return judge(left->left, right->right) && judge(left->right, right->left);
    }
};
