// Runtime: 40 ms, faster than 20.54% of C++ online submissions for Count Complete Tree Nodes.
// Memory Usage: 28.5 MB, less than 100.00% of C++ online submissions for Count Complete Tree Nodes.
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
    int countNodes(TreeNode* root) {
        if (root == NULL)
            return 0;
        int l = root->left != NULL ? countNodes(root->left) : 0;
        int r = root->right != NULL ? countNodes(root->right) : 0;
        return l + 1 + r;
    }
};
