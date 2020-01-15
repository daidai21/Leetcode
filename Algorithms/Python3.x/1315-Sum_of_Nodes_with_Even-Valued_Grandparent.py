# DFS
# Runtime: 120 ms, faster than 15.99% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        self.DFS(root)
        return self.res

    def DFS(self, node):
        if not node:
            return
        if node.val % 2 == 0:
            self.add_grandson(node)
        self.DFS(node.left)
        self.DFS(node.right)

    def add_grandson(self, node):
        if not node:
            return 
        for son_node in [node.left, node.right]:
            if son_node:
                for grandson_node in [son_node.left, son_node.right]:
                    if grandson_node:
                        self.res += grandson_node.val
