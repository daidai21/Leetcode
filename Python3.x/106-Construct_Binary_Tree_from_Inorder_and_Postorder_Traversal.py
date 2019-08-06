# Runtime: 196 ms, faster than 37.61% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Memory Usage: 88.2 MB, less than 7.14% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:])
        return root
