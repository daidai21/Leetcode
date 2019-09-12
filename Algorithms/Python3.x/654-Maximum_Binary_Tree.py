# Runtime: 224 ms, faster than 40.92% of Python3 online submissions for Maximum Binary Tree.
# Memory Usage: 14 MB, less than 40.00% of Python3 online submissions for Maximum Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        node = TreeNode(max(nums))
        idx = nums.index(max(nums))
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return node
