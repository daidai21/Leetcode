# Runtime: 440 ms, faster than 65.38% of Python3 online submissions for Longest Univalue Path.
# Memory Usage: 17.8 MB, less than 5.43% of Python3 online submissions for Longest Univalue Path.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.recursion(root)
        return self.res

    def recursion(self, node):
        if not node:
            return 0
        left_length = self.recursion(node.left)
        right_length = self.recursion(node.right)
        left, right = 0, 0
        if node.left and node.left.val == node.val:
            left = left_length + 1
        if node.right and node.right.val == node.val:
            right = right_length + 1
        self.res = max(self.res, left + right)
        return max(left, right)
