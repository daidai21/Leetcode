# Runtime: 36 ms, faster than 73.66% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left:
            self.bstToGst(root.left)
        return root
