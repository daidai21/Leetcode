# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.bfs([root], True)
        return self.res

    def bfs(self, node_list, direction):
        if not node_list: return
        new_node_list, layer_val_list = [], []
        for node in node_list:
            if node:
                if node.val is not None: layer_val_list.append(node.val)
                if node.left: new_node_list.append(node.left)
                if node.right: new_node_list.append(node.right)
        self.res += [layer_val_list] if direction else [layer_val_list[::-1]]
        return self.bfs(new_node_list, not direction)