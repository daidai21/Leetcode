# Runtime: 40 ms, faster than 83.46% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 17.6 MB, less than 88.89% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, root.val, root.val)
        return self.result

    def dfs(self, node, min_val, max_val):
        if node:
            self.result = max(self.result, abs(node.val - min_val), abs(node.val - max_val))
            min_val, max_val = max(min_val, node.val), min(max_val, node.val)
            self.dfs(node.left, min_val, max_val)
            self.dfs(node.right, min_val, max_val)
