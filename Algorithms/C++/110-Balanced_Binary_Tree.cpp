/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return getHeight(root) >= 0;
    }

    int getHeight(TreeNode* root) {
        if (root == nullptr) return 0;
        int leftHeight = getHeight(root->left),
            rightHeight = getHeight(root->right);
        if (leftHeight >= 0 && rightHeight >= 0 && std::abs(leftHeight - rightHeight) <= 1) return std::max(leftHeight, rightHeight) + 1;
        return -1;
    }
};
