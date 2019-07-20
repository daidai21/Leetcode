# Runtime: 56 ms, faster than 63.82% of Python3 online submissions for Lowest Common Ancestor of Deepest Leaves.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of Deepest Leaves.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.recursion(root)[1]

    def recursion(self, node):
        if not node:
            return 0, None
        level_left, node_left = self.recursion(node.left)
        level_right, node_right = self.recursion(node.right)
        if level_left > level_right:
            return level_left + 1, node_left
        elif level_left < level_right:
            return level_right + 1, node_right
        else:
            return level_left + 1, node
