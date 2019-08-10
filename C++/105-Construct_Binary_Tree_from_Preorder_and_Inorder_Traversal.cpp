// Runtime: 32 ms, faster than 19.35% of C++ online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
// Memory Usage: 16.6 MB, less than 85.71% of C++ online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build_tree(preorder, inorder, 0, preorder.size(), 0, inorder.size());
    }
private:
    TreeNode* build_tree(vector<int>& preorder, vector<int>& inorder, 
                         int pre_l, int pre_r, int in_l, int in_r) {
        if (pre_l >= pre_r || in_l >= in_r)
            return NULL;
        int dis = 0;
        for (int i = in_l; in_l < in_r; ++dis, ++i)
            if (preorder[pre_l] == inorder[in_l + dis])
                break;
        TreeNode* node = new TreeNode(preorder[pre_l]);
        node->left = build_tree(preorder, inorder, pre_l + 1, pre_l + dis + 1, 
                                                   in_l, in_l + dis);
        node->right = build_tree(preorder, inorder, pre_l + dis + 1, pre_r,
                                                    in_l + dis + 1, in_r);
        return node;
    }
};
