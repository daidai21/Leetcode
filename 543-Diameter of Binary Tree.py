# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        self.n = 1
        self.depth(root)
        return self.n - 1

    def depth(self, node):
        if not node: return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.n = max(self.n, left + right + 1)
        return max(left, right) + 1
