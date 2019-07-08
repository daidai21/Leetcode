# dfs
# Runtime: 92 ms, faster than 97.90% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 20 MB, less than 100.00% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    current_max = float('-inf')
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        self.max_path_sum(root)
        return self.current_max

    def max_path_sum(self, root):
        if not root: return 0
        left = self.max_path_sum(root.left)
        right = self.max_path_sum(root.right)
        if left < 0: left = 0
        if right < 0: right = 0
        self.current_max = max(left + right + root.val, self.current_max)
        return max(left, right) + root.val
