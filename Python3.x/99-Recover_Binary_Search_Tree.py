# Runtime: 80 ms, faster than 44.41% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Recover Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre_node = TreeNode(float("-inf"))
        self.first, self.second = None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, node):
        if not node:
            return 
        self.inorder(node.left)
        if not self.first and self.pre_node.val > node.val:  # the first time occurs reversed order
            self.first, self.second = self.pre_node, node
        if self.first and self.pre_node.val > node.val:  # the first or second time occurs reversed order
            self.second = node
        self.pre_node = node
        self.inorder(node.right)
