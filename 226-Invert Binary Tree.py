# 递归
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 12.4 MB, less than 0.96% of Python3 online submissions for Invert Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root: root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
