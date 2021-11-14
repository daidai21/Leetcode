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
    int minDepth(TreeNode* root) {
        // 1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr) return 1;
        // 2.如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度      
        int minLeft = minDepth(root->left),
            minRight = minDepth(root->right);
        // 这里其中一个节点为空，说明minLeft和minRight有一个必然为0，所以可以返回m1 + m2 + 1;
        if (root->left == nullptr || root->right == nullptr) return minLeft + minRight + 1;
        // 3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
        return std::min(minLeft, minRight) + 1;
    }
};
