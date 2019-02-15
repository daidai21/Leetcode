# Runtime: 152 ms, faster than 80.14% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 51.5 MB, less than 100.00% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

