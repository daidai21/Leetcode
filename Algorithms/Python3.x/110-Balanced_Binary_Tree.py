# Runtime: 52 ms, faster than 94.10% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 17.8 MB, less than 89.13% of Python3 online submissions for Balanced Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        self.get_height(root)
        return self.flag

    def get_height(self, node):
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right) + 1
