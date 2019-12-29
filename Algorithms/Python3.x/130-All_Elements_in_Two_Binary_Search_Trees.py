# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.res = []
        self.recursion(root1)
        self.recursion(root2)
        self.res.sort()
        return self.res

    def recursion(self, node):
        if not node:
            return 
        else:
            self.res.append(node.val)
            if node.left:
                self.recursion(node.left)
            if node.right:
                self.recursion(node.right)
            return 
