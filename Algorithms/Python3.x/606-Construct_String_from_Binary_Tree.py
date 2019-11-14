# untime: 56 ms, faster than 80.86% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Construct String from Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        else:
            if not t.left and not t.right:
                return str(t.val) + ""
            if not t.left and t.right:
                return str(t.val) + "()(" + self.tree2str(t.right) + ")"
            if t.left and not t.right:
                return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"
