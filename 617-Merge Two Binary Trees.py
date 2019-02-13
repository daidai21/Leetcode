# 直接将t2加到t1上
# Runtime: 80 ms, faster than 99.96% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 13.1 MB, less than 0.79% of Python3 online submissions for Merge Two Binary Trees.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if not t1: return t2
        if not t2: return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
