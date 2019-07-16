# Runtime: 36 ms, faster than 66.27% of Python3 online submissions for Same Tree.
# Memory Usage: 13.3 MB, less than 21.62% of Python3 online submissions for Same Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if (p is None) != (q is None):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and (p.val == q.val)
