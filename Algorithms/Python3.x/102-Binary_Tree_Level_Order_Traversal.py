# bfs 队列
# Runtime: 40 ms, faster than 98.37% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 12.5 MB, less than 0.86% of Python3 online submissions for Binary Tree Level Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root: return []
        queue, result = [], []
        queue.append(root)
        while len(queue) > 0:
            line, tmp = [], []
            for node in queue:
                line.append(node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            result.append(line)
        return result
