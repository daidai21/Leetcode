# Runtime: 64 ms, faster than 98.58% of Python3 online submissions for Delete Node in a BST.
# Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Delete Node in a BST.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return 
        if root.val == key:
            if root.left:
                # Find the right of most leaf of the left sub-tree
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                # Attach right child to the right of that leaf
                left_right_most.right = root.right
                # Return left child instead of root, delete root
                return root.left
            else:
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
