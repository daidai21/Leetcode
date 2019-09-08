# Runtime: 36 ms, faster than 82.58% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 13.6 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.res = []
        self.bfs([root])
        return self.res

    def bfs(self, layer):
        if layer == []:
            return
        new_layer = []
        flag = False  # is add node.val?
        for node in layer:
            if node and not flag:
                self.res.append(node.val)
                flag = True
            if node.right:
                new_layer.append(node.right)
            if node.left:
                new_layer.append(node.left)
        self.bfs(new_layer)
