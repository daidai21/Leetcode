# 
# Runtime: 44 ms, faster than 96.86% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root
        if not tmp.left: return None  # 节点的左指针为空不执行
        tmp = tmp.left  # 
        while tmp.right: tmp = tmp.right
        tmp.right = root.right  # 
        root.right = root.left  # 左指针转换到右边
        root.left = None  # 节点左指针置空

'''
前序遍历（中左右）
'''
