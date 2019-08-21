// Runtime: 32 ms, faster than 88.56% of C++ online submissions for Convert BST to Greater Tree.
// Memory Usage: 23.5 MB, less than 71.43% of C++ online submissions for Convert BST to Greater Tree.
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
    TreeNode* convertBST(TreeNode* root) {
        if (!root)
            return root;
        convertBST(root->right);
        total += root->val;
        root->val = total;
        convertBST(root->left);
        return root;
    }
private:
    int total = 0;
};
