# DFS
# Runtime: 32 ms, faster than 50.30% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Leaf-Similar Trees.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf_seq(root1) == self.leaf_seq(root2)

    def leaf_seq(self, root):
        res = []
        def DFS(node):
            if node is None:
                return 
            if node.left is None and node.right is None:
                res.append(node.val)
            if node.left is not None:
                DFS(node.left)
            if node.right is not None:
                DFS(node.right)

        DFS(root)
        return res
