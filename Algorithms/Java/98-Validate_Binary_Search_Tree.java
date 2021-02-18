// 前序迭代
// Runtime: 1 ms, faster than 33.49% of Java online submissions for Validate Binary Search Tree.
// Memory Usage: 38.7 MB, less than 56.91% of Java online submissions for Validate Binary Search Tree.
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        Stack<TreeNode> stk = new Stack<>();
        Long prev = Long.MIN_VALUE;
        while (stk.empty() == false || root != null) {
            while (root != null) {
                stk.push(root);
                root = root.left;
            }
            root = stk.pop();
            if (root.val <= prev) {
                return false;
            }
            prev = Long.valueOf(root.val);
            root = root.right;
        }
        return true;
    }
}
