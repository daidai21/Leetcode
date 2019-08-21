// Runtime: 40 ms, faster than 58.57% of C++ online submissions for Merge Two Binary Trees.
// Memory Usage: 19.1 MB, less than 30.56% of C++ online submissions for Merge Two Binary Trees.
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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 && t2) {
            TreeNode* result = new TreeNode(t1->val + t2->val);
            result->left = mergeTrees(t1->left, t2->left);
            result->right = mergeTrees(t1->right, t2->right);
            return result;
        } else 
            return t1 ? t1 : t2;
    }
};
