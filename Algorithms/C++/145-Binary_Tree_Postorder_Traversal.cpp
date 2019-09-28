// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Postorder Traversal.
// Memory Usage: 9.1 MB, less than 96.77% of C++ online submissions for Binary Tree Postorder Traversal.
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> portorder;
        stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            if (node) {
                portorder.push_back(node->val);
                stack.push(node->left);
                stack.push(node->right);
            }
        }
        reverse(portorder.begin(), portorder.end());
        return portorder;
    }
};
