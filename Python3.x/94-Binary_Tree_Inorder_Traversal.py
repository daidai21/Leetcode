'''
中序遍历二叉树
'''


# 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result = []
        def recursion(result, node):
            if node:
                recursion(result, node.left)
                result.append(node.val)
                recursion(result, node.right)

        recursion(result, root)
        return result


# 迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: return result
            node = stack.pop()
            result.append(node.val)
            root = node.right
