# recursion
# Runtime: 48 ms, faster than 19.18% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        else:
            node = TreeNode(preorder[0])
            node.left  = self.bstFromPreorder([v for v in preorder[1:] if v < preorder[0]])
            node.right = self.bstFromPreorder([v for v in preorder[1:] if v > preorder[0]])
            return node
