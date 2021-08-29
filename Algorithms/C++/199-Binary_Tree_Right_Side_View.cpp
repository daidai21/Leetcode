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
    vector<int> rightSideView(TreeNode* root) {
        std::vector<TreeNode*> layer = { root };
        std::vector<int> result;
        while (!layer.empty()) {
            std::vector<TreeNode*> nextLayer;
            bool foundEndNode = false;
            for (int i = layer.size() - 1; i >= 0; --i) {
                if (layer[i] != nullptr) {
                    if (!foundEndNode) {
                        result.push_back(layer[i]->val);
                        foundEndNode = true;
                    }
                    nextLayer.push_back(layer[i]->right);
                    nextLayer.push_back(layer[i]->left);
                }
            }
            layer = nextLayer;
            std::reverse(layer.begin(), layer.end());
        }
        return result;
    }
};
