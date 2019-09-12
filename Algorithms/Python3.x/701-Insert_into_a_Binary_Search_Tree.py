# Iterative
# Runtime: 120 ms, faster than 88.44% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.1 MB, less than 8.00% of Python3 online submissions for Insert into a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        curr = root
        while True:
            if curr.val <= val:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            else:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
        return root
