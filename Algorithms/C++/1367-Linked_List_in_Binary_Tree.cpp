// Runtime: 40 ms, faster than 23.61% of C++ online submissions for Linked List in Binary Tree.
// Memory Usage: 32 MB, less than 82.09% of C++ online submissions for Linked List in Binary Tree.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (head == NULL) return true;
        if (root == NULL) return false;
        return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
    
    bool dfs(ListNode* head, TreeNode* root) {
        if (head == NULL) return true;
        if (root == NULL) return false;
        return head->val == root->val && 
            (dfs(head->next, root->left) || dfs(head->next, root->right));
    }
};
