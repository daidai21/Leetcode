// 递归
// Runtime: 8 ms, faster than 94.19% of C++ online submissions for Validate Binary Search Tree.
// Memory Usage: 21.5 MB, less than 95.33% of C++ online submissions for Validate Binary Search Tree.
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
    bool isValidBST(TreeNode* root) {
        return validate(root, LONG_MIN, LONG_MAX);
    }

private:
    bool validate(TreeNode* node, long int low, long int high) {
        if (node == nullptr) {
            return true;
        }
        if (node->val <= low || node->val >= high) {
            return false;
        }
        return validate(node->right, node->val, high) &&
            validate(node->left, low, node->val);
    }
};


// 前序递归
// Runtime: 8 ms, faster than 94.19% of C++ online submissions for Validate Binary Search Tree.
// Memory Usage: 21.5 MB, less than 95.33% of C++ online submissions for Validate Binary Search Tree.
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
    bool isValidBST(TreeNode* root) {
        this->prev = LONG_MIN;
        return inorder(root);
    }

private:
    bool inorder(TreeNode* node) {
        if (node == nullptr) {
            return true;
        }
        if (inorder(node->left) == false) {
            return false;
        }
        if (node->val <= this->prev) {
            return false;
        }
        this->prev = node->val;
        return inorder(node->right);
    }
    
    long int prev;
};
