# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        def recursion(node, is_root):
            if not node:
                return None
            node_deleted = node.val in to_delete_set
            if is_root and not node_deleted:
                res.append(node)
            node.left = recursion(node.left, node_deleted)
            node.right = recursion(node.right, node_deleted)
            return None if node_deleted else node
        
        recursion(root, True)
        return res

