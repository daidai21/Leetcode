// Runtime: 4 ms, faster than 93.88% of C++ online submissions for Flatten Binary Tree to Linked List.
// Memory Usage: 9.6 MB, less than 100.00% of C++ online submissions for Flatten Binary Tree to Linked List.
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
    void flatten(TreeNode* root) {
        if (root == NULL)
            return;
        flatten(root->left);
        flatten(root->right);
        TreeNode* temp = root;
        if (temp->left == NULL)
            return;
        temp = temp->left;
        while (temp->right)
            temp = temp->right;
        temp->right = root->right;
        root->right = root->left;
        root->left = NULL;
    }
};
