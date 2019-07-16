// Runtime: 4 ms, faster than 69.76% of C++ online submissions for Same Tree.
// Memory Usage: 9.7 MB, less than 81.05% of C++ online submissions for Same Tree.
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL)
            return true;
        if ((p == NULL) != (q == NULL))
            return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right) && (p->val == q->val);
    }
};