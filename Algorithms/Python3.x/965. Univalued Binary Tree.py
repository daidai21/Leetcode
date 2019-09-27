# iterator
# Runtime: 32 ms, faster than 95.42% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Univalued Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != val:
                return False
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return True
