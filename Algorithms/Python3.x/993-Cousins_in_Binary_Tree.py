# Runtime: 44 ms, faster than 23.23% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 13.9 MB, less than 6.12% of Python3 online submissions for Cousins in Binary Tree.
# dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_depth = self.find_depth(root, x, 0)
        self.x_parent = self.find_parent(root, x)
        self.y_depth = self.find_depth(root, y, 0)
        self.y_parent = self.find_parent(root, y)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent

    def find_depth(self, node, target, depth):
        if node is not None and node.val == target:
            return depth + 1
        left = self.find_depth(node.left, target, depth + 1) if node.left is not None else None
        right = self.find_depth(node.right, target, depth + 1) if node.right is not None else None
        return left or right

    def find_parent(self, node, target):
        if node is not None and node.left is not None and node.left.val == target:
            return node
        if node is not None and node.right is not None and node.right.val == target:
            return node
        left = self.find_parent(node.left, target) if node.left is not None else None
        right = self.find_parent(node.right, target) if node.right is not None else None
        return left or right
