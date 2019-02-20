# 
# Runtime: 52 ms, faster than 99.74% of Python3 online submissions for House Robber III.
# Memory Usage: 14.5 MB, less than 96.61% of Python3 online submissions for House Robber III.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: 'TreeNode') -> 'int':
        return self.dfs(root)[1]

    def dfs(self, node):
        if node is None: return (0, 0)
        left, right = self.dfs(node.left), self.dfs(node.right)
        return (left[1] + right[1], max(left[1] + right[1], left[0] + right[0] + node.val))


'''
max(left[1] + right[1], left[0] + right[0] + node.val) 算是状态转移方程
    left[1] + right[1] 同一个父节点的两个节点
    left[0] + right[0] + node.val 两个孙子和一个爷爷
'''
