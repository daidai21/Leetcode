# Runtime: 60 ms, faster than 6.48% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Binary Tree Pruning.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left  = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            root = None
        return root
