// Runtime: 0 ms, faster than 100.00% of C online submissions for Maximum Difference Between Node and Ancestor.
// Memory Usage: 8.7 MB, less than 100.00% of C online submissions for Maximum Difference Between Node and Ancestor.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int max(int n1, int n2) { return n1 > n2 ? n1 : n2; }
int min(int n1, int n2) { return n1 < n2 ? n1 : n2; }


void dfs(struct TreeNode* node, int max_val, int min_val, int* p_result) {
    if (node != NULL) {
        *p_result = max(*p_result, abs(node->val - min_val));
        *p_result = max(*p_result, abs(node->val - max_val));
        max_val = max(max_val, node->val);
        min_val = min(min_val, node->val);
        dfs(node->left, max_val, min_val, p_result);
        dfs(node->right, max_val, min_val, p_result);
    }
    return ;
}


int maxAncestorDiff(struct TreeNode* root){
    int result = 0;
    dfs(root, root->val, root->val, &result);
    return result;
}
