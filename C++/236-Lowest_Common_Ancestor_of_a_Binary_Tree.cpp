// Runtime: 20 ms, faster than 72.12% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
// Memory Usage: 16.6 MB, less than 94.55% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL || root == p || root == q)
            return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        return left && right ? root : left ? left : right;
    }
};
