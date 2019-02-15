# s的每个节点为起点与t匹配
# Runtime: 232 ms, faster than 71.08% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        return self.traverse(s, t)

    def equals(self, x, y):
        if x is None and y is None: return True
        if x is None or y is None: return False
        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)

    def traverse(self, s, t):
        return s is not None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))


# s的每个节点为起点与t匹配
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        if not s: return
        if self.check(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t): return True
        return False

    def check(self, s, t):
        if s is None and t is None: return True
        if s is None or t is None: return False
        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)
