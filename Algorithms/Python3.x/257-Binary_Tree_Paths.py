# Runtime: 40 ms, faster than 61.41% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 13.7 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.dfs(root, "")
        return self.res

    def dfs(self, node, curr):
        if not node:
            return
        if not node.left and not node.right:
            self.res.append(curr + str(node.val))
        if node.left:
            self.dfs(node.left, curr + str(node.val) + "->")
        if node.right:
            self.dfs(node.right, curr + str(node.val) + "->")
