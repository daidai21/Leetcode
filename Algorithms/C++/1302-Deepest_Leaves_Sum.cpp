// BFS
// Runtime: 48 ms, faster than 73.18% of C++ online submissions for Deepest Leaves Sum.
// Memory Usage: 33.7 MB, less than 100.00% of C++ online submissions for Deepest Leaves Sum.
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
    int deepestLeavesSum(TreeNode* root) {
        vector<TreeNode* > layer = {root};
        int res = 0;
        while (layer.size()) {
            vector<TreeNode* > next_layer;
            int next_res = 0;
            for (TreeNode* node : layer) {
                next_res += node->val;
                if (node->left)
                    next_layer.push_back(node->left);
                if (node->right)
                    next_layer.push_back(node->right);
            }
            layer = next_layer;
            res = next_res;
        }
        return res;
    }
};
