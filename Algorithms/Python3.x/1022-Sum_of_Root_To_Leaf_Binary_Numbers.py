# Runtime: 28 ms, faster than 99.63% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, node, cur_val):
        if not node:
            return
        if node.left is None and node.right is None:
            self.result += cur_val * 2 + node.val
        if node.left:
            self.dfs(node.left, cur_val * 2 + node.val)
        if node.right:
            self.dfs(node.right, cur_val * 2 + node.val)
