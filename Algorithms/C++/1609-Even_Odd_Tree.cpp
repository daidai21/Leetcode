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
    bool isEvenOddTree(TreeNode* root) {
        vector<TreeNode*> layer = {root};
        int layer_num = 0;
        while (layer.size() > 0) {
            vector<TreeNode*> next_layer;
            int cur_val = layer[0]->val;
            for (int i = 0; i < layer.size(); ++i) {
                // judge sorted
                if (i > 0) {                    
                    if (layer_num % 2 == 0) {
                        // increasing
                        if (layer[i]->val <= cur_val) {
                            cout << "DEBUG 1 " << cur_val << layer_num << endl;
                            return false;
                        }
                    } else {
                        // decreasing
                        if (layer[i]->val >= cur_val) {
                            cout << "DEBUG 2" << endl;
                            return false;
                        }
                    }
                    cur_val = layer[i]->val;
                }
                // judge odd or even
                if ((layer_num % 2 == 0 && layer[i]->val % 2 != 1) || 
                    (layer_num % 2 == 1 && layer[i]->val % 2 != 0)) {
                    return false;
                }
                // for next layer
                if (layer[i]->left != nullptr) {
                    next_layer.push_back(layer[i]->left);
                }
                if (layer[i]->right != nullptr) {
                    next_layer.push_back(layer[i]->right);
                }
            }
            layer = next_layer;
            layer_num++;
        }
        return true;
    }
};
