# Runtime: 36 ms, faster than 73.16% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.8 MB, less than 6.52% of Python3 online submissions for Binary Tree Preorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
