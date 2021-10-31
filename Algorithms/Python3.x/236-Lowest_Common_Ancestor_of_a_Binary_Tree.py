# recurse
# Runtime: 80 ms, faster than 95.30% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 28.1 MB, less than 14.83% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.result = None
        def recurse_tree(current_node):
            if not current_node: return False  # 如果已经是根节点返回False
            left = recurse_tree(current_node.left)  # 左分支递归
            right = recurse_tree(current_node.right)  # 右分支递归
            mid = current_node == p or current_node == q  # 如果当前节点就是p或者q
            if mid + left + right >= 2: self.result = current_node  # 如果任意两个flag为True都改变result
            return mid or left or right

        recurse_tree(root)
        return self.result


# recurse
# Runtime: 136 ms, faster than 9.19% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 41.3 MB, less than 5.01% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, 2)]  # 2是两边都未遍历，1是左边遍历完成，0是左右边两边遍历完成
        one_node_found = False
        LCA_index = -1  # （Lowest Common Ancestors），即最近公共祖先指向公共祖先索引
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != 0:
                if parent_state == 2:  # 两边都未遍历
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]  # p或q为公共祖先的情况
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:  # 左边已经遍历，右边没有遍历
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, 2))
            else:  # 左右边两边遍历完成
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        return None



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
