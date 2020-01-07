# BFS
# Runtime: 52 ms, faster than 46.19% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        layer = [root]
        while layer:
            next_layer = []
            vals = []
            for node in layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
                vals.append(node.val)
            layer = next_layer
            res.append(sum(vals) / len(vals))
        return res
