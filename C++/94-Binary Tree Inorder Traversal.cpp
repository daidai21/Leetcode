// Runtime: 4 ms, faster than 62.50% of C++ online submissions for Binary Tree Inorder Traversal.
// Memory Usage: 9.5 MB, less than 31.86% of C++ online submissions for Binary Tree Inorder Traversal.
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
    vector<int> inorderTraversal(TreeNode* root) {
        recursion(res, root);
        return res;
    }
private:
    vector<int> res;
    void recursion(vector<int>& res, TreeNode* root) {
        if (root == NULL)
            return;
        if (root->left != NULL)
            recursion(res, root->left);
        if (root->val != NULL)
            res.push_back(root->val);
        if (root->right != NULL)
            recursion(res, root->right);
    }
};


// Runtime: 4 ms, faster than 62.50% of C++ online submissions for Binary Tree Inorder Traversal.
// Memory Usage: 9.1 MB, less than 95.59% of C++ online submissions for Binary Tree Inorder Traversal.
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> todo;
        while (root != NULL || !todo.empty()) {
            while (root) {
                todo.push(root);
                root = root->left;
            }
            root = todo.top();
            todo.pop();
            res.push_back(root->val);
            root = root->right;
        }
        return res;
    }
};
