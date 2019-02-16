# 
# Runtime: 44 ms, faster than 96.86% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root
        if not tmp.left: return None
        tmp = tmp.left
        while tmp.right: tmp = tmp.right
        tmp.right = root.right
        root.right = root.left
        root.left = None
# 先将左右子树压平，然后将左子树嵌入到本节点与右子树之间。

