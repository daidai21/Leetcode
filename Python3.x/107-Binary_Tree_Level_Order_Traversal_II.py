# Runtime: 44 ms, faster than 60.11% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 14.1 MB, less than 6.72% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        self.res, self.queue = [], [root]
        self.bfs()
        return self.res[::-1]

    def bfs(self):
        if self.queue == []:
            return 
        new_queue, layer_val = [], []
        for node in self.queue:
            if node.val is not None:
                layer_val.append(node.val)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        self.res.append(layer_val)
        self.queue = new_queue
        return self.bfs()