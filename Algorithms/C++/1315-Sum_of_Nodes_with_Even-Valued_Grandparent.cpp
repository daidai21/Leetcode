// DFS
// Runtime: 52 ms, faster than 48.16% of C++ online submissions for Sum of Nodes with Even-Valued Grandparent.
// Memory Usage: 31.3 MB, less than 100.00% of C++ online submissions for Sum of Nodes with Even-Valued Grandparent.
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
    int sumEvenGrandparent(TreeNode* root) {
        res_ = 0;
        DFS(root);
        return res_;
    }

    void DFS(TreeNode* node) {
        if (node == nullptr)
            return ;
        if (node->val % 2 == 0)
            add_grandson(node);
        DFS(node->left);
        DFS(node->right);
    }

    void add_grandson(TreeNode* node) {
        if (node == nullptr)
            return ;
        for (TreeNode* son_node : {node->left, node->right}) {
            if (son_node != nullptr) {
                for (TreeNode* grandson_node : {son_node->left, son_node->right})
                    if (grandson_node != nullptr)
                        res_ += grandson_node->val;
            }
        }
    }

private:
    int res_;
};
