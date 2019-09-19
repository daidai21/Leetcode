// recursion
// Runtime: 8 ms, faster than 34.08% of C++ online submissions for Construct Binary Search Tree from Preorder Traversal.
// Memory Usage: 10.8 MB, less than 95.24% of C++ online submissions for Construct Binary Search Tree from Preorder Traversal.
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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        return recursion(preorder, INT_MAX);
    }
private:
    int index = 0;
    TreeNode* recursion(vector<int>& preorder, int upper) {
        if (index == preorder.size() || preorder[index] > upper)
            return NULL;
        TreeNode* node = new TreeNode(preorder[index++]);
        node->left  = recursion(preorder, node->val);
        node->right = recursion(preorder, upper);
        return node;
    }
};
