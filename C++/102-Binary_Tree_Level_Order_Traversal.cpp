// Runtime: 4 ms, faster than 93.37% of C++ online submissions for Binary Tree Level Order Traversal.
// Memory Usage: 16.1 MB, less than 5.63% of C++ online submissions for Binary Tree Level Order Traversal.
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL)
            return res;
        vector<TreeNode*> layers = {root};
        bfs(res, layers);
        return res;
    }
private:
    vector<vector<int>> res;
    void bfs(vector<vector<int>>& res, vector<TreeNode*> layers) {
        if (layers.size() == 0)
            return;
        vector<TreeNode*> new_layers;
        vector<int> layer_value;
        for (TreeNode* node : layers) {
            if (node->left != NULL)
                new_layers.push_back(node->left);
            if (node->right != NULL)
                new_layers.push_back(node->right);
            layer_value.push_back(node->val);
        }
        res.push_back(layer_value);
        bfs(res, new_layers);
    }
};