# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root


"""INPUT
[1,3,3,3,2]
3
[1,2,null,2,null,2]
2
[1,1,1]
1
[1,2,3]
1

OUTPUT
[1,null,3,null,4]
[1,3,null,null,2]
[1]
[]
[1,2,3]
"""
