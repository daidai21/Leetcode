# Runtime: 68 ms, faster than 57.61% of Python3 online submissions for Minimum Absolute Difference in BST.
# Memory Usage: 16 MB, less than 33.33% of Python3 online submissions for Minimum Absolute Difference in BST.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.values = []
        self.dfs(root)
        self.values.sort()
        min_diff = float("inf")
        for i in range(1, len(self.values)):
            min_diff = min(min_diff, self.values[i] - self.values[i - 1])
        return min_diff

    def dfs(self, node):
        if node is None:
            return 
        self.values.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
