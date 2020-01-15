# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        layer = [root]
        res = root.val
        while layer:
            next_layer = []
            next_res = 0
            for node in layer:
                next_res += node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            layer = next_layer
            res = next_res
        return res
