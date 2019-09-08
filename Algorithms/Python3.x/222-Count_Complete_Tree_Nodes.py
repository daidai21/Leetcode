# Runtime: 100 ms, faster than 47.09% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.6 MB, less than 6.90% of Python3 online submissions for Count Complete Tree Nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return (self.countNodes(root.left) if root.left is not None else 0) + 1 + (self.countNodes(root.right) if root.right is not None else 0)
