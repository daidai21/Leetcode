# Runtime: 92 ms, faster than 42.29% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18 MB, less than 5.55% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root
