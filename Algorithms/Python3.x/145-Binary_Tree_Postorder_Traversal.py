# recursoin
# Runtime: 36 ms, faster than 74.54% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.9 MB, less than 5.72% of Python3 online submissions for Binary Tree Postorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.postorder = []
        self.recursion(root)
        return self.postorder

    def recursion(self, node):
        if not node:
            return 
        if node.left:
            self.recursion(node.left)
        if node.right:
            self.recursion(node.right)
        if node.val is not None:
            self.postorder.append(node.val)


# Runtime: 36 ms, faster than 74.54% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.7 MB, less than 5.72% of Python3 online submissions for Binary Tree Postorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                postorder.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return reversed(postorder)
