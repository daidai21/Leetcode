# Runtime: 52 ms, faster than 99.88% of Python3 online submissions for Binary Tree Tilt.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Binary Tree Tilt.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0
        self.recursion(root)
        return self.total_tilt

    def recursion(self, node):
        if node is None:
            return 0
        left_val = self.recursion(node.left)
        right_val = self.recursion(node.right)
        self.total_tilt += abs(left_val - right_val)
        return left_val + right_val + node.val
