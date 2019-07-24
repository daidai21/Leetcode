# Runtime: 364 ms, faster than 8.70% of Python3 online submissions for All Possible Full Binary Trees.
# Memory Usage: 27.6 MB, less than 5.30% of Python3 online submissions for All Possible Full Binary Trees.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        N -= 1
        if N == 0:
            return [TreeNode(0)]
        res = []
        for l in range(1, min(20, N), 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    root = TreeNode(0)
                    root.left, root.right = left, right
                    res += [root]
        return res
