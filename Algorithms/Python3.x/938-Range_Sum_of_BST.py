# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.helper(root, L, R, 0)

    def helper(self, node, L, R, value):
        if node:
            value = self.helper(node.left, L, R, value)
            if L <= node.val <= R:
                value += node.val
            value = self.helper(node.right, L, R, value)
        return value
